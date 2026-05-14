# 图像生成和编辑工具 (FLUX.2 Klein)

基于 `Flux2KleinPipeline` 的图像生成和编辑工具，支持文本提示、参考服装图、掩码等功能。

## 环境要求

- Python 3.8+
- PyTorch 2.0+
- diffusers 库
- PIL (Pillow)
- CUDA GPU（推荐，有助于加速）

## 基本用法

```bash
python main.py "提示词" [选项]
```

## 参数说明

### 必需参数

| 参数 | 说明 |
|-----|------|
| `prompt` | 文本提示，描述要生成或修改的内容 |

### 输入/输出参数

| 参数 | 说明 |
|-----|------|
| `--input`, `-i` | 输入图像路径（支持多个），用于图像编辑 |
| `--output`, `-o` | 输出图像路径，默认为 `E:\wdj\output\output.png` |
| `--clothing-ref` | 参考服装图片路径，需要与 `--input` 配合使用 |
| `--mask` | 可选的掩码图片路径（白色=编辑区域，黑色=保留原图） |

### 尺寸控制参数

| 参数 | 说明 |
|-----|------|
| `--width` | 输出图像宽度（仅在无输入图时生效），默认 96 |
| `--height` | 输出图像高度（仅在无输入图时生效），默认 96 |
| `--scale` | 缩放比例，针对输入图像（如 0.5 = 50%，1.5 = 150%） |

### 生成参数

| 参数 | 说明 |
|-----|------|
| `--steps` | 推理步数，默认 4（步数越多，质量越好但速度越慢） |
| `--seed` | 随机种子（-1=随机种子，>=0=固定种子），默认 -1（随机） |
| `--num-images`, `-n` | 生成图像数量，默认 1 |

## 使用示例

### 1. 从文本提示生成图像
```bash
python main.py "一只坐在椅子上的猫，油画风格" --output cat.png --width 512 --height 512
```

### 2. 编辑现有图像
```bash
python main.py "把猫变成狗" --input original.jpg --output dog.jpg
```

### 3. 按参考服装换装
```bash
python main.py "保持人物面部特征不变" --input person.jpg --clothing-ref outfit.jpg --output result.jpg --width 200 --height 200
```

### 4. 按比例缩放输入图像
```bash
python main.py "增大眼睛" --input face.jpg --scale 0.8 --output result.jpg
```

### 5. 使用掩码编辑特定区域
```bash
python main.py "更换衣服颜色为蓝色" --input person.jpg --mask clothing_mask.png --output result.jpg
```

### 6. 生成多张图像（随机种子）
```bash
python main.py "美丽的风景画" --output landscape.png --width 512 --height 512 --num-images 3
```
输出文件：`landscape_12345.png`, `landscape_2_67890.png`, `landscape_3_11111.png`（种子随机）

### 7. 组合多个参数
```bash
python main.py "高质量照片，增加细节" \
  --input input.jpg \
  --clothing-ref style.jpg \
  --output result.jpg \
  --scale 1.2 \
  --steps 12 \
  --seed 1 \
  --num-images 2
```

## 输出格式

- 输出路径以 `.jpg` 或 `.jpeg` 结尾：使用 JPEG 格式保存（质量 85）
- 输出路径以其他格式结尾（如 `.png`）：使用对应格式保存
- 如果生成多张图像，后续图像会在文件名中添加后缀（`_2`, `_3` 等）
- 每张图像的文件名会包含其使用的种子值，如 `result_12345.jpg`

## 提示

### 关于参考服装换装
- 需要同时指定 `--input`（要编辑的人物）和 `--clothing-ref`（参考服装）
- 脚本会自动将参考图像与人物图像一起传给模型，让模型学习衣服风格
- 可选参数 `--mask` 可以进一步控制只编辑衣服部分

### 关于尺寸
- 编辑图像时，输出尺寸由 `--scale` 或 `--width/--height` 控制
- 不指定尺寸参数时，输出尺寸等同于输入图像尺寸
- 建议使用 `--scale` 保持原始宽高比

### 关于性能
- `--steps` 越高，生成质量越好，但耗时更长（推荐 4-12）
- 在 CUDA GPU 上运行速度明显快于 CPU
- `--seed` 为 -1 时使用随机种子，每张图片结果不同；指定具体值时结果可重现

### 关于提示词
- 提示词越详细，生成结果越接近预期
- 使用英文通常效果更好，也支持中文
- 可在提示词中明确不希望改变的部分，如"保持面部特征不变"

## 常见问题

**Q：生成的图像与输入图像尺寸不符？**
A：检查是否指定了 `--scale` 或 `--width/--height`，确认参数值是否正确。

**Q：编辑效果不理想？**
A：尝试增加 `--steps` 的值（如 8-12），并优化提示词描述。

**Q：输出文件过大？**
A：使用 `.jpg` 作为输出格式会更节省空间，或在输出路径中指定 `.jpg` 而非 `.png`。

**Q：可以同时指定 `--scale` 和 `--width/--height` 吗？**
A：不建议。如同时指定，`--scale` 会优先使用。

**Q：如何让每张图片都不同？**
A：默认使用随机种子（--seed -1），每张图片会生成不同的变体。

**Q：如何重现相同结果？**
A：指定固定种子，如 `--seed 42`，相同条件下会生成相同结果。

## 输出示例

成功运行后会打印：
```
Loading model from local snapshot: ...
Saved image to E:\wdj\output\result.jpg
```

错误示例：
```
ValueError: --clothing-ref requires --input to specify the source person image
```
说明需要同时指定 `--input` 才能使用 `--clothing-ref`。
