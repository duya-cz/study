import os
# 从操作系统中获得环境变量，再获取到APIkey

from openai import OpenAI
# 并不是直接进行调用OpenAI，而是通过一个第三方OpenAI库创建一个客户端对象来管理请求，而不是直接调用 HTTP API。
# 所以，第一次使用OpenAI库是，需要通过pip3 install openai来安装
# 下载是来源于PyPI，这是Python的官方包管理系统，提供了大量的第三方库和工具，可以通过pip命令来安装和管理这些库。
# pip是Python的包管理工具，可以用来安装和管理Python库和工具。提供了对Python包的查找、下载、安装、卸载等功能


client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    # 不建议将APIkey直接写在代码中，应该使用环境变量来保护敏感信息
    # environ是环境变量的简写，os.environ.get()方法用于获取环境变量的值。这里获取的也就是DEEPSEEK的APIkey
    
    base_url="https://api.deepseek.com/v1"
)

# 进行交互 
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {
            "role": "system",
            "content": "你是一个数学计算助手，帮我进行数学计算"
        },
        {
            "role": "user",
            "content": "163减18等于多少？请只输出数字结果。"
        }
    ],
    stream=False
)
# response是包含模型回复的一个对象，choice[0]就是主要负责语言回复的那一块，message.content就是回复的内容
print(response.choices[0].message.content)