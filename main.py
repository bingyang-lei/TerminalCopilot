import os
import argparse
import sys
import warnings
from utils.ArgParser import argparser
from openai import OpenAI
from openai.types.chat import ChatCompletionChunk
args = argparser()

url1 = 'http://localhost:11434/v1/'
url2 = "http://localhost:11435/v1/"  # 如果采用多模型对话则要使用多个端口,并export OLLAMA_HOST="0.0.0.0:11435"

client = OpenAI(
    base_url = url1,
    api_key='ollama', # required, but unused
)
# llama3.2:1b, llama3.1:8b, qwen2.5, deepseek-r1:32b
REASONING_MODEL = 'deepseek-r1:32b'  # 推理模式使用模型
FINALMODEL = REASONING_MODEL if args.reasoning else args.model
FINALMODEL = args.model
PPT_SYSTEM_PROMPT = "下面请你根据用户的描述，生成符合要求的PPT，输出为markdown格式，遵循reveal.js的要求。"
conversation_history = [{"role": "system", "content": "You are a helpful assistant."}]

def talk_mode(initial_prompt: str, max_rounds: int, model1: str, model2: str = None):
    """
    对话模式核心逻辑（支持双模型对话）
    """
    global conversation_history
    
    current_model = model1
    current_content = initial_prompt
    conversation_history = []  # 重置对话历史
    
    for round in range(max_rounds):
        print(f"\n\U0001F4E9 Round {round+1}/{max_rounds}")
        
        # 添加用户输入到对话历史
        conversation_history.append({"role": "user", "content": current_content})
        
        try:
            # 创建聊天完成请求
            stream = client.chat.completions.create(
                model=current_model,
                messages=conversation_history,
                temperature=0.7,
                max_tokens=4096,
                stream=True
            )
            
            # 处理流式响应
            full_response, current_content = stream_response(stream, current_model)
            
            # 更新对话历史
            conversation_history.append({"role": "assistant", "content": full_response})
            
            # 切换模型（如果启用双模型）
            if model2:
                current_model = model2 if current_model == model1 else model1
                client.base_url = url2 if client.base_url == url1 else url1
        
        except Exception as e:
            print(f"\n\033[31mError: {str(e)}\033[0m")
            break

def stream_response(stream, current_model=None, display=True):
    full_response = ""
    global FINALMODEL
    if current_model:
        FINALMODEL = current_model
    if display:
        print(f"\n🤖 {FINALMODEL}:", end="", flush=True)
    
    try:
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                content = chunk.choices[0].delta.content
                if display:
                    print(content, end="", flush=True)
                full_response += content
        if display:
            print("\n")
        return full_response, full_response  # 返回完整响应和下一轮输入
    except Exception as e:
        print(f"\n\033[31mStream Error: {str(e)}\033[0m")
        return full_response, full_response

def main():
    global conversation_history
    pipe_input = ""
    if not sys.stdin.isatty():
        pipe_input = str(sys.stdin.buffer.read())
        print(f"接受管道输入成功")
    tty_fd = os.open('/dev/tty', os.O_RDONLY)
    sys.stdin = os.fdopen(tty_fd, 'r')

    if args.ppt:
        conversation_history[0]["content"] = PPT_SYSTEM_PROMPT
    
    if args.talk:
        initial_prompt = args.talk[0]
        try:
            max_rounds = int(args.talk[1])
        except ValueError:
            print("\033[31m错误：轮数必须为整数\033[0m")
            return
        
        model2 = args.model2 if args.model2 else None
        talk_mode(initial_prompt, max_rounds, FINALMODEL, model2)
    else:
        while True:
            try:
                user_input = input("\n\U0001F4AC Your question (exit to quit): ")
                if user_input.lower() in ["exit", "quit", "q"]:
                    break
                user_input = pipe_input + user_input
                pipe_input = ''
                # 更新对话历史
                conversation_history.append({"role": "user", "content": user_input})

                if args.reasoning:  # 新增推理模式分支
                    # 第一阶段：生成思考步骤
                    user_input + '我的问题如上所示，请你分步分析并认真思考我的需求，输出清晰的解决步骤（不要直接回答）'
                    conversation_history.append({"role": "user", "content": user_input})
                    print(f"\n⏰ 思考中...")
                    stream = client.chat.completions.create(
                        model=FINALMODEL,
                        messages=conversation_history,
                        temperature=0.7,
                        max_tokens=4096,
                        stream=True
                    )
                    step1_response, _ = stream_response(stream,display=False)
                    print(f"✨ 思考结束 ✨")
                    # 第二阶段：生成最终答案
                    conversation_history.extend([
                        {"role": "assistant", "content": step1_response},
                        {"role": "user", "content": "请基于上述思考步骤，给出专业严谨的最终解答"}
                    ])
                    
                    stream = client.chat.completions.create(
                        model=FINALMODEL,
                        messages=conversation_history,
                        temperature=0.5, # 第二阶段，降低温度，以获得更稳定的回答
                        max_tokens=4096,
                        stream=True
                    )
                    step2_response, _ = stream_response(stream)
                    conversation_history.append({"role": "assistant", "content": step2_response})
                else:
                    # 创建聊天完成请求
                    stream = client.chat.completions.create(
                        model=FINALMODEL,
                        messages=conversation_history,
                        temperature=0.7,
                        max_tokens=4096,
                        stream=True
                    )
                    
                    # 处理流式响应
                    full_response, _ = stream_response(stream)
                    
                    # 更新对话历史
                    conversation_history.append({"role": "assistant", "content": full_response})
            
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"\n\033[31mError: {str(e)}\033[0m")
                break

if __name__ == "__main__":
    main()