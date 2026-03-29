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

# 目前仅支持侧边栏修改模型指令，对话指令效果无法反馈在侧边栏
if "partner_name" not in st.session_state:
    st.session_state.partner_name = ""

if "partner_character" not in st.session_state:
    st.session_state.partner_character = ""

if "ConMemory" not in st.session_state:
    st.session_state.Conmemory = []


st.title("AI 简单伴侣")
st.logo("😀")

# 左侧侧边栏 with 上下文管理器，后续写的都是sidebar的内容
with st.sidebar:
    st.subheader("AI 伴侣")
    partner_name=st.text_input("昵称",placeholder="请输入昵称", value=st.session_state.partner_name)
    partner_character=st.text_input("性格",placeholder="请输入性格", value=st.session_state.partner_character)
    
    if partner_name:
        st.session_state.partner_name=partner_name

    if partner_character:
        st.session_state.partner_character=partner_character

system_prompt = f"""
你叫{partner_name}，现在是用户的真实伴侣，请完全代入伴侣角色。：
规则：
    1. 每次只回1条消息
    2. 禁止任何场景或状态描述性文字
    3. 匹配用户的语言
    4. 回复简短，像微信聊天一样
    5. 有需要的话可以用❤️🌸等emoji表情
    6. 用符合伴侣性格的方式对话
    7. 回复的内容，要充分体现伴侣的性格特征
伴侣性格：
    - {partner_character}
你必须严格遵守上述规则来回复用户。
"""

client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com/v1"
)

for record in st.session_state.Conmemory:
    st.chat_message(record["role"]).write(record["content"])

prompt = st.chat_input("请输入您要问的问题？")
if prompt is not None:
    st.chat_message("user").write(prompt)
    
    st.session_state.Conmemory.append({"role": "user", "content": prompt})
    
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            *st.session_state.Conmemory
        ],
        stream=True
    )

    st.empty()
    response.messages = st.empty()

    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            full_response += chunk.choices[0].delta.content
            response.messages.chat_message("assistant").write(full_response)

    st.session_state.Conmemory.append({"role": "assistant", "content": full_response})
