# print("构建一个 Bot: 🤖 + ⚙️ + 🧠")
# print("\U0001F4AC")
import os
import requests
import json
import argparse
import sys
from openai import OpenAI
a = [1,2,3]
b = [4,5,6]
print(a+b)
# client = OpenAI(
#     base_url = 'http://localhost:11434/v1/',
#     api_key='ollama', # required, but unused
# )

# response = client.chat.completions.create(
#   model="qwen2.5",
#   messages=[
#     {"role": "system", "content": "You are a helpful assistant."},
#     {"role": "user", "content": "Who won the world series in 2020?"},
#     {"role": "assistant", "content": "The LA Dodgers won in 2020."},
#     {"role": "user", "content": "Where was it played?"}
#   ]
# )
# print(response.choices[0].message.content)



# try:
#     # Unix系统直接读取终端设备
#     with open('/dev/tty', 'r') as tty:
#         user = input("\n\U0001F4AC 请输入你的问题（输入exit退出）: ")
# except (FileNotFoundError, PermissionError):
#     # Windows系统回退到标准input（可能无法交互）
#     user = input("\n\U0001F4AC 请输入你的问题（输入exit退出222）: ")
# import pyautogui
# import os
# import sys
# import argparse
# # a = binary_data = sys.stdin.buffer.read()
# # print(a)
# parser = argparse.ArgumentParser()
# parser.add_argument('-t','--talk', nargs=2, metavar=('PROMPT', 'ROUNDS'), 
#                     help='Start dialogue mode with initial prompt and max rounds')

# args = parser.parse_args()
# print(args.talk)
# if args.talk:
#     print("yes")

# print(args.talk[0])
# # 获取当前文件所在目录
# current_dir = os.path.dirname(os.path.abspath(__file__))

# # 截取屏幕
# screenshot = pyautogui.screenshot()

# # 保存截图到当前目录
# screenshot_path = os.path.join(current_dir, "screenshot.png")
# screenshot.save(screenshot_path)

# print(f"截图已保存到: {screenshot_path}")