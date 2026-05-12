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
    parser.add_argument("--output", "-o", default=str(DEFAULT_OUTPUT), help="Output image path")
    parser.add_argument("--height", type=int, default=96, help="Generated image height when no input image is used")
    parser.add_argument("--width", type=int, default=96, help="Generated image width when no input image is used")
    parser.add_argument("--steps", type=int, default=4, help="Number of inference steps")
    parser.add_argument("--seed", type=int, default=0, help="Random seed")
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


def numbered_output_path(output_path, index):
    if index == 0:
        return output_path

    return output_path.with_name(f"{output_path.stem}_{index + 1}{output_path.suffix}")


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

    call_args = {
        "prompt": args.prompt,
        "num_inference_steps": args.steps,
    }

    if args.input:
        images = [load_image(input_path) for input_path in args.input]
        call_args["image"] = images if len(images) > 1 else images[0]
    else:
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
        image_args = dict(call_args)
        image_args["generator"] = torch.Generator(device=device).manual_seed(args.seed + index)

        image = pipe(**image_args).images[0]
        current_output_path = numbered_output_path(output_path, index)
        image.save(current_output_path)
        print(f"Saved image to {current_output_path}")


if __name__ == "__main__":
    main()
