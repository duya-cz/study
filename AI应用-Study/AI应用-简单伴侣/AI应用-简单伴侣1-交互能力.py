import streamlit as st
import os
from openai import OpenAI

st.set_page_config(
    page_title="AI简单伴侣",  # 网页标题
    page_icon="AI",          # 网页图标
    layout="wide",                  # 页面布局
    initial_sidebar_state="expanded",# 侧边栏默认状态   
    menu_items={}
)

# 大标题
st.title("AI简单伴侣")

# logo
st.logo("😀")

# 创建大模型交互的客户端
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com/v1"
)

# 系统提示词
system_prompt = "你是一个智能AI伴侣，请回答我的问题"

# 储存会话消息
if "ConMemory" not in st.session_state:
    st.session_state.ConMemory = []
# st.session_state是streamlit用于保存会话记忆的方法
# ConMemory是对其自定义的一个键名，用于储存模型与用户的会话消息
# ConMemory后边.append()方法，就是给这个键加上值，也就是模型和用户的会话消息
# st.session_state是容器，是字典，ConMemory是里面的一个键，值是一个列表，列表里存储了模型和用户的会话消息，每条消息都是一个字典，包含角色和内容

# 展示聊天记录 定义自变量record，遍历展示会话存储中的记录
for record in st.session_state.ConMemory:
    st.chat_message(record["role"]).write(record["content"])
    # if record["role"] == "user":
    #     st.chat_message("user").write(record["content"])
    # else:
    #     st.chat_message("assistant").write(record["content"])
# （目前仅仅只是展示记录的能力，没有记忆的智能能力）

# 消息输入框
prompt = st.chat_input("请输入您要问的问题？")
if prompt:
    st.chat_message("user").write(prompt)
    
    # 保存用户输入的会话消息
    st.session_state.ConMemory.append({"role": "user", "content": prompt})
    
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": prompt
        }
        ],
        stream=False
    )
# 输出结果
    print("<------>" + response.choices[0].message.content)
    st.chat_message("assistant").write(response.choices[0].message.content)
   
    # 保存模型回复的会话消息
    st.session_state.ConMemory.append({"role": "assistant", "content": response.choices[0].message.content})
