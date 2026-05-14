import argparse
import os
from pathlib import Path

os.environ.setdefault("HF_HOME", "E:/HuggingFaceCache")

import torch
from diffusers import Flux2KleinPipeline
from diffusers.utils import load_image


MODEL_ID = "black-forest-labs/FLUX.2-klein-4B"
DEFAULT_OUTPUT = Path(r"E:\wdj\output\output.png")
MODEL_CACHE_NAME = "models--black-forest-labs--FLUX.2-klein-4B"
MODEL_CACHE_DIRS = [
    Path(os.environ["HF_HOME"]) / "hub" / MODEL_CACHE_NAME / "snapshots",
    Path.home() / ".cache" / "huggingface" / "hub" / MODEL_CACHE_NAME / "snapshots",
]


def build_parser():
    parser = argparse.ArgumentParser(description="Generate or edit an image with FLUX.2 klein 4B.")
    parser.add_argument("prompt", help="Text prompt, for example: Turn this cat into a dog")
    parser.add_argument("--input", "-i", nargs="+", help="Optional local paths or URLs of images to edit")
    parser.add_argument("--clothing-ref", help="Reference image path for clothing style or outfit")
    parser.add_argument("--mask", help="Optional mask image path for the clothing region (white = edit area, black = keep original)")
    parser.add_argument("--output", "-o", default=str(DEFAULT_OUTPUT), help="Output image path")
    parser.add_argument("--height", type=int, default=96, help="Generated image height when no input image is used")
    parser.add_argument("--width", type=int, default=96, help="Generated image width when no input image is used")
    parser.add_argument("--scale", type=float, help="Scale factor for input images, e.g. 0.5 for 50% of original size")
    parser.add_argument("--steps", type=int, default=4, help="Number of inference steps")
    parser.add_argument("--seed", type=int, default=-1, help="Random seed (-1 for random seeds, >=0 for fixed seed)")
    parser.add_argument("--num-images", "-n", type=int, default=1, help="Number of images to generate")
    return parser


def find_cached_model_path():
    for snapshots_dir in MODEL_CACHE_DIRS:
        if not snapshots_dir.exists():
            continue

        snapshots = [
            path for path in snapshots_dir.iterdir()
            if path.is_dir() and (path / "model_index.json").exists()
        ]
        if snapshots:
            return max(snapshots, key=lambda path: path.stat().st_mtime)

    return None


def load_pipeline(dtype):
    cached_model_path = find_cached_model_path()
    if cached_model_path:
        print(f"Loading model from local snapshot: {cached_model_path}")
        return Flux2KleinPipeline.from_pretrained(cached_model_path, torch_dtype=dtype)

    try:
        print("Loading model from local cache...")
        return Flux2KleinPipeline.from_pretrained(
            MODEL_ID,
            torch_dtype=dtype,
            local_files_only=True,
        )
    except Exception as ex:
        print(f"Local cache load failed: {ex}")
        print("Loading model from Hugging Face Hub...")
        return Flux2KleinPipeline.from_pretrained(MODEL_ID, torch_dtype=dtype)


def generate_filename_from_prompt(prompt):
    """根据prompt内容生成文件名 - 提取着装信息，控制在6字以内"""
    import re
    
    # 查找着装关键词
    clothing_keywords = ['身着', '穿着', '穿', '身穿']
    
    for keyword in clothing_keywords:
        if keyword in prompt:
            # 找到关键词后的内容
            start_idx = prompt.find(keyword) + len(keyword)
            # 提取到下一个标点或空格
            clothing_part = prompt[start_idx:].split('，')[0].split(' ')[0].strip()
            
            # 清理特殊字符
            clothing_part = re.sub(r'[\\/:*?"<>|，。！？；]', '', clothing_part)
            
            # 限制在6个字以内
            if len(clothing_part) > 6:
                clothing_part = clothing_part[:6]
            
            if clothing_part:
                return clothing_part
    
    # 如果找不到着装信息，使用原来的逻辑
    cleaned = re.sub(r'[\\/:*?"<>|，。！？；]', '', prompt)
    parts = cleaned.split('，')
    main_part = parts[0].strip()
    
    if len(main_part) > 6:
        main_part = main_part[:6]
    
    filename = main_part.strip() if main_part else "generated_image"
    
    return filename


def numbered_output_path(output_path, index, seed):
    stem = output_path.stem
    suffix = output_path.suffix
    if index == 0:
        return output_path.with_name(f"{stem}_{seed}{suffix}")
    else:
        return output_path.with_name(f"{stem}_{index}_{seed}{suffix}")


def save_output_image(image, output_path):
    output_path = Path(output_path)
    if output_path.suffix.lower() in {".jpg", ".jpeg"}:
        if image.mode in ("RGBA", "LA"):
            image = image.convert("RGB")
        image.save(output_path, quality=85)
    else:
        image.save(output_path)


def main():
    args = build_parser().parse_args()
    if args.num_images < 1:
        raise ValueError("--num-images must be at least 1")

    has_cuda = torch.cuda.is_available()
    device = "cuda" if has_cuda else "cpu"
    dtype = torch.bfloat16

    pipe = load_pipeline(dtype)
    if has_cuda:
        pipe.enable_model_cpu_offload()
    else:
        pipe.to(device)

    prompt = args.prompt
    if args.clothing_ref:
        if not args.input:
            raise ValueError("--clothing-ref requires --input to specify the source person image")
        prompt = f"{prompt}，根据参考服装图片换装，包括袜子" if prompt else "根据参考服装图片换装，包括袜子"

    call_args = {
        "prompt": prompt,
        "num_inference_steps": args.steps,
    }

    if args.input:
        from PIL import Image
        images = [load_image(input_path) for input_path in args.input]
        
        # 计算目标尺寸
        target_width, target_height = None, None
        if args.scale:
            # 按比例缩放
            first_img = images[0]
            target_width = int(first_img.width * args.scale)
            target_height = int(first_img.height * args.scale)
        elif args.width != 96 or args.height != 96:
            # 使用指定的绝对尺寸
            target_width, target_height = args.width, args.height
        
        # 如果有目标尺寸，resize 输入图像
        if target_width is not None and target_height is not None:
            resized_images = []
            for img in images:
                resized_img = img.resize((target_width, target_height), Image.LANCZOS)
                resized_images.append(resized_img)
            images = resized_images
        
        if args.clothing_ref:
            clothing_ref_image = load_image(args.clothing_ref)
            # 使用相同的目标尺寸 resize 参考图像
            if target_width is not None and target_height is not None:
                clothing_ref_image = clothing_ref_image.resize((target_width, target_height), Image.LANCZOS)
            images.append(clothing_ref_image)
        
        call_args["image"] = images if len(images) > 1 else images[0]
        
        if args.mask:
            mask_image = load_image(args.mask)
            # 使用相同的目标尺寸 resize mask
            if target_width is not None and target_height is not None:
                mask_image = mask_image.resize((target_width, target_height), Image.LANCZOS)
            call_args["mask"] = mask_image
    else:
        # 没有输入图像时，生成新图
        if args.scale:
            raise ValueError("--scale only works with --input images")
        call_args.update({
            "height": args.height,
            "width": args.width,
            "guidance_scale": 1.0,
        })

    # 如果output是默认值，根据prompt生成文件名
    if args.output == str(DEFAULT_OUTPUT):
        filename = generate_filename_from_prompt(args.prompt)
        output_path = DEFAULT_OUTPUT.parent / f"{filename}.png"
    else:
        output_path = Path(args.output)
    
    output_path.parent.mkdir(parents=True, exist_ok=True)

    for index in range(args.num_images):
        import random
        if args.seed == -1:
            current_seed = random.randint(0, 2**32 - 1)
        else:
            current_seed = args.seed + index
        
        image_args = dict(call_args)
        image_args["generator"] = torch.Generator(device=device).manual_seed(current_seed)

        image = pipe(**image_args).images[0]
        current_output_path = numbered_output_path(output_path, index, current_seed)
        save_output_image(image, current_output_path)
        print(f"Saved image to {current_output_path}")


if __name__ == "__main__":
    main()
