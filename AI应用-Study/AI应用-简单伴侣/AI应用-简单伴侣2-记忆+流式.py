import streamlit as st
import os
from openai import OpenAI

st.set_page_config(
    page_title="AI 简单伴侣",
    page_icon="AI",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)

st.title("AI 简单伴侣")

st.logo("😀")

client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com/v1"
)

system_prompt = "你是一个智能 AI 伴侣，请回答我的问题"

if "ConMemory" not in st.session_state:
    st.session_state.ConMemory = []

for record in st.session_state.ConMemory:
    st.chat_message(record["role"]).write(record["content"])

prompt = st.chat_input("请输入您要问的问题？")
if prompt:
    st.chat_message("user").write(prompt)
    
    st.session_state.ConMemory.append({"role": "user", "content": prompt})
    
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            *st.session_state.ConMemory
            # 解包操作，将原本conMemory列表中的元素，拆成一个一个元素，传递给messages参数(实现记忆能力)
        ],
        # 非流式输出
        # stream=False
        
        # 流式输出
        stream=True
    )
    # 非流式输出解析方式
    # st.chat_message("assistant").write(response.choices[0].message.content)
    
    # 流式输出解析方式
    # 流式输出就是content字段每次输出一个字符，所以我们需要进行追加
    st.empty() # 空容器，占位符，用于更新叠加内容
    response.messages = st.empty() # 定义一个空容器，用于展示模型回复的内容

    
    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content: # 判断content字段是否为空，有东西才叠加输出
            full_response += chunk.choices[0].delta.content
            response.messages.chat_message("assistant").write(full_response)
            #相当于这个for循环每次叠加的内容，都在这个空容器中，相当于界面中是一条消息一个字一个字输出
            # 用这一个空容器输出模型的每次回复叠加（避免模型一次回复一个字符，一次字符两个字符的叠加）

    st.session_state.ConMemory.append({"role": "assistant", "content": full_response})