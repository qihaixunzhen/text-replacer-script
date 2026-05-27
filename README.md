# text-replacer-script

一个简单的文本替换工具集，用于将文本文件中的指定内容替换为目标内容。通过配置文件管理替换规则，支持批量替换。

## 项目结构

| 文件 | 说明 |
|------|------|
| [replace.py](replace.py) | Python 核心替换脚本 |
| [config.txt](config.txt) | 替换规则配置文件 |
| [replace_mac.sh](replace_mac.sh) | macOS 调用脚本 |
| [replace_win.bat](replace_win.bat) | Windows 调用脚本 |

## 各脚本功能

### replace.py — Python 核心替换脚本

读取配置文件中的替换规则，对目标文件执行全局文本替换。

**用法：**
```bash
python3 replace.py <目标文件>          # 使用默认 config.txt
python3 replace.py <目标文件> <配置>    # 使用指定配置文件
```

**参数说明：**
- 第一个参数（必需）：要修改的文本文件路径
- 第二个参数（可选）：配置文件路径，不指定则使用同目录下的 `config.txt`

### config.txt — 替换规则配置文件

每行格式为 `被替换的文字>替换成的文字`，例如：
```
old_word>new_word
hello>world
foo>bar
```
- 空行和不合法的行会自动忽略
- 多个规则按顺序依次应用到文件

### replace_mac.sh — macOS 调用脚本

适用于 macOS / Linux 系统的 shell 脚本，已添加可执行权限。

**用法：**
```bash
./replace_mac.sh <目标文件>
```

### replace_win.bat — Windows 调用脚本

适用于 Windows 系统的批处理脚本。

**用法（在 cmd 中运行）：**
```cmd
replace_win.bat <目标文件>
```

## 使用示例

假设 `example.txt` 内容为：
```
Hello old_word, welcome to old_word world! Say hello to everyone.
```

**macOS / Linux：**
```bash
./replace_mac.sh example.txt
```

**Windows：**
```cmd
replace_win.bat example.txt
```

运行后 `example.txt` 变为：
```
Hello new_word, welcome to new_word world! Say world to everyone.
```

## 注意事项

- 替换是全局的，所有匹配项都会被替换
- 默认区分大小写
- 目标文件会被原地修改（直接覆盖原文件）
