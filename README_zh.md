# TCP: 终端 Copilot 🚀

你的 AI 命令行伴侣。
(this file is generated from `cat README.md | tcp`)

<details>
    <summary>Demo</summary>
    <img src="./photos/show.gif" alt="tcp Demo">
</details>

基于 **Unix 哲学** 构建，你可以通过管道传递任何内容。

![示例](./photos/image.png)

（说实话，我觉得这个 README 有点哗众取宠了，TCP 还有许多功能需要添加或改进，但显然AI自我感觉良好🥺）

## 🚀 功能

### 定制的AI助手
- **多模型选择**  
  `-m qwen2.5` | `--model deepseek-r1:32b`
  切换不同的 LLM , 就像切换 shell
- **推理模式** (`-r`)
  两阶段批判性思维：  
  `分析 → 执行`，两阶段采用不同参数设置
- **PPT 生成模式** (`-p`)  
  在终端生成演示文稿级的 markdown
- **双模型对话** (`--model2 llama3.1:8b`)  
  模型 vs 模型的辩论
- **加入其他你自己的功能**  
  基于 TCP 构建你的个性化 AI 助手

### **原生终端魔法**
- **管道力量**  
  ```bash
  ls -la | tcp -m qwen2.5 "解释这些文件权限"
  man grep | tcp -r "总结关键标志"
  ```
- **对话模式** (`-t`)  
  ```bash
  tcp -t "调试这个 Python 脚本" 5
  ```
- **上下文感知**
  维护会话历史，像你最喜欢的 shell 那样

## 🛠️ 安装

### **先决条件**
- Python 3.9+
- [Ollama](https://ollama.ai/) 运行中

```bash
# 快速克隆
git clone https://github.com/bingyang-lei/TerminalCopilot.git && cd TerminalCopilot

# 安装依赖（推荐使用 virtualenv）
pip install -r requirements.txt

# 启动 AI 引擎
ollama serve &  # 在后台运行

# 拉取你喜欢的模型
ollama pull qwen2.5 deepseek-r1:32b

# （可选）设置别名
echo 'alias tcp="python /yourpath/main.py"' >> ~/.bashrc
source ~/.bashrc
```

## 📚 用法

<details>
<summary>命令行参数</summary>

```commandline
usage: main.py [-h] [-m MODEL] [--model2 MODEL2] [-r] [-p] [-t PROMPT ROUNDS]

options:
  -h, --help            show this help message and exit
  -m MODEL, --model MODEL
                        Designate a model to use, default is qwen2.5
  --model2 MODEL2       (option) Choosing another model to talk with final model
  -r, --reasoning       Enable reasoning mode(more powerful but slower)
  -p, --ppt             enter PPT generation mode
  -t PROMPT ROUNDS, --talk PROMPT ROUNDS
                        Start dialogue mode with initial prompt and max rounds
```
</details>

## 🤔 为什么选择 tcp？

### **Unix 哲学的体现**
```bash
# 链接到经典工具
find . -name "*.py" | tcp -r "分析代码模式"
netstat -tulpn | tcp "解释这些网络连接"
man sh | tcp "给我更友好的手册"
```
---

<!-- **献给终端战士们**  \n[贡献](#) | [文档](#) | [赞助](#) -->