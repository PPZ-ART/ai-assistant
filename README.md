# AI 助手

一个基于 DeepSeek 大模型的命令行 AI 对话机器人，支持多轮对话与上下文记忆。

## 功能

- 连续对话，AI 能记住上下文
- 可自定义 AI 人设（修改 system prompt）

## 运行方法

1. 设置环境变量 `DEEPSEEK_KEY` 为你的 API Key
2. 运行 `python main.py`

## 技术栈

- Python 3
- DeepSeek API（HTTP 调用）
- urllib / json / os
