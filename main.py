import os
import urllib.request
import json

# 从环境变量读 Key（代码里绝不写明文钥匙）
密钥 = os.environ.get("DEEPSEEK_KEY")
if 密钥 is None:
    print("错误：没找到 DEEPSEEK_KEY 环境变量。")
    print("请先在终端运行：$env:DEEPSEEK_KEY='sk-你的key'")
    exit()

网址 = "https://api.deepseek.com/chat/completions"

# 对话记录：一个列表，装每一条消息（每条是一个字典）
对话记录 = [
    {"role": "system", "content": "你是一个友好的助手，用简洁的中文回答。"}
]

def 问AI():
    数据 = json.dumps({
        "model": "deepseek-chat",
        "messages": 对话记录
    }).encode("utf-8")
    请求 = urllib.request.Request(
        网址, data=数据,
        headers={
            "Authorization": "Bearer " + 密钥,
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(请求) as 响应:
        结果 = json.loads(响应.read().decode("utf-8"))
    return 结果["choices"][0]["message"]["content"]

print("AI 助手已上线，输入“退出”结束")
while True:
    问题 = input("\n你：")
    if 问题 == "退出":
        print("再见！")
        break
    对话记录.append({"role": "user", "content": 问题})
    回答 = 问AI()
    对话记录.append({"role": "assistant", "content": 回答})
    print("AI：", 回答)
