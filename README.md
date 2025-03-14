# TCP: TerminalCopilot 🤖⌨️

Your AI-powered command line companion, built with **Unix philosophy** at its core.

![example](./photos/image.png)
![tcp Demo](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbGQ5eHlqN3V2dWk2Z3B2dGJ6MG0yYzRzc3l4NHJvNnV2dW4xYjRzYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/26n6WjCA3ZRmQnRl6/giphy.gif)

(To be honest, I admit this README is a little showy, and there are many features of TCP that need to be added or improved🥺)
## 🌟 Features That Will Blow Your Terminal Away

### **AI Superpowers**
- 🧠 **Multi-Model Mastery**  
  `-m qwen2.5` | `--model deepseek-r1:32b`  
  Switch between cutting-edge LLMs like changing shells
- 🕵️ **Reasoning Mode** (`-r`)  
  Two-stage critical thinking:  
  `Analyze → Execute` with different temperature settings
- 💼 **PPT Gen Mode** (`-p`)  
  Create presentation-ready markdown in terminal
- 🎭 **Dual Model Dialogues**  
  `--model2 llama3.1:8b` for model vs model debates
- 🛠️ **Adding any other features by your own**
  Build your personalized AI assistant based on TCP

### **Terminal Native Magic**
- 🛠️ **Pipeline Power**  
  ```bash
  ls -la | tcp -m qwen2.5 "Explain these file permissions"
  man grep | tcp -r "Summarize key flags"
  ```
- 🔄 **Conversation Mode** (`-t`)  
  ```bash
  tcp -t "Debug this Python script" 5
  ```
- 📜 **Context-Aware**  
  Maintains session history like your favorite shell

## 🚀 Installation 

**Prerequisites**: Python 3.9+, [Ollama](https://ollama.ai/) running

```bash
# Clone with speed
git clone https://github.com/bingyang-lei/TerminalCopilot.git && cd TerminalCopilot

# Install dependencies (virtualenv recommended)
pip install -r requirements.txt

# Start your AI engine
ollama serve &  # Keep running in background

# Pull models you like
ollama pull qwen2.5 deepseek-r1:32b

# (Optional) set alias
echo 'alias tcp="python /yourpath/main.py"' >> ~/.bashrc
source ~/.bashrc
```

## 💡 Why tcp?

### **Unix Philosophy Embodied**

```bash
# Chain with classic tools
find . -name "*.py" | tcp -r "Analyze code patterns"
netstat -tulpn | tcp "Explain these network connections"
man sh | tcp "Give me a more friendly manual"
```
---

<!-- **Made with ❤️ for terminal warriors**  
[Contribute](#) | [Docs](#) | [Sponsor](#) -->
