import requests
API_KEY = "key"
API_URL = "https://api.siliconflow.cn/v1/chat/completions"
MODEL = "deepseek-ai/DeepSeek-V2.5"
response = requests.post(
    API_URL,
    headers={"Authorization": f"Bearer {API_KEY}"},
    json={
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "你是一个客服助手，回答简洁。"},
            {"role": "user", "content": "你好，请问你们营业时间是几点？"}
        ]
    }
)

print("状态码：", response.status_code)
print("AI 回答：")
print(response.json()["choices"][0]["message"]["content"])