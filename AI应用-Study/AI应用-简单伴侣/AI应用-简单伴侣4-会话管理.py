import streamlit as st
import os
from openai import OpenAI
from datetime import datetime
import json

# 获取脚本所在目录
script_dir = os.path.dirname(os.path.abspath(__file__))
# 创建会话目录
sessions_dir = os.path.join(script_dir, "sessions")


st.set_page_config(
    page_title="AI 简单伴侣",
    page_icon="AI",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)

# 生产会话标识时间函数
def TimeID():
    return datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

# 目前仅支持侧边栏修改模型指令，对话指令效果无法反馈在侧边栏
# 昵称
if "partner_name" not in st.session_state:
    st.session_state.partner_name = ""

# 性格
if "partner_character" not in st.session_state:
    st.session_state.partner_character = ""

# 会话记录
if "ConMemory" not in st.session_state:
    st.session_state.ConMemory = []

# 会话时间标识
if "ConTime" not in st.session_state:
    st.session_state.ConTime = TimeID()
# 保存会话信息函数
def save_session():
    # 进行判断，如果没有新的指令或对话，就不创建新的文件
    if (not st.session_state.ConMemory and 
        not st.session_state.partner_name and 
        not st.session_state.partner_character):
        return
    

    if st.session_state.ConTime:
        dataCon={
            "partner_name":st.session_state.partner_name,
            "partner_character":st.session_state.partner_character,
            "ConMemory":st.session_state.ConMemory,
            "ConTime":st.session_state.ConTime
        }
        # 如果session目录不存在则创建
        if not os.path.exists(sessions_dir):
          os.mkdir(sessions_dir)

        # 保存会话数据
        # 使用 os.path.join 拼接路径
        file_path = os.path.join(sessions_dir, st.session_state.ConTime + ".json")
        with open(file_path, "w", encoding="utf-8") as f:
            # 使用 json.dump 保存会话数据
            json.dump(dataCon, f, ensure_ascii=False, indent=2)

# 读取所有会话历史数据函数
def load_sessions():
    # 创建一个空列表，用于存储会话数据
    session_list=[]
    # 判断存储会话数据的目录是否存在
    if os.path.exists(sessions_dir):
        # 列表 获取存储会话数据的目录下的所有文件名
        file_list = os.listdir(sessions_dir)
        # 遍历列表中的每个文件名
        for file_name in file_list:
            # 检查文件名是否是以.json结尾，只处理该类型文件
            if file_name.endswith(".json"):
                # 获取当前该文件的绝对路径（目录地址+文件名形成的文件路径）
                file_path = os.path.join(sessions_dir, file_name)
                # 读当前文件，获取文件内容
                with open(file_path, "r", encoding="utf-8") as f:
                    # 将json文件内容转化为python可操作的字典格式，并创建对象
                    data = json.load(f)
                    # 将当前的会话数据添加到会话列表中
                    session_list.append(data)
    
    # 将数据进行倒序排序并返回调用
    session_list.sort(reverse=True)
    return session_list

# 删除会话函数
def delete_session(con_time):
    # os.path.join是字符拼接函数，在目录路径下，找到文件con_time+后缀形成要删除的json文件完整路径
    file_path=os.path.join(sessions_dir, con_time+".json")
    # 检查是否存在该文件
    if os.path.exists(file_path):
        # 删除该文件
        os.remove(file_path)
    # 删除成功True，否则删除失败False
        return True
    return False


st.title("AI 简单伴侣")
st.logo("😀")

# 左侧侧边栏 with 上下文管理器，后续写的都是sidebar的内容
with st.sidebar:

    st.text("历史会话")
    # 获取所有会话
    session_list = load_sessions()
    # 遍历所有会话
    for session in session_list:
        HisButton1,HisButton2=st.columns([4,1])

        # 加载会话信息
        with HisButton1:
        #    创建注明该历史会话时间标识的按钮
           if st.button(session["ConTime"],width="stretch",icon="📄",key=f"load_{session['ConTime']}"):
            #  加载更改会话信息
               st.session_state.ConTime=session["ConTime"]
               st.session_state.ConMemory = session.get("ConMemory", [])
               st.session_state.partner_name = session.get("partner_name", "")
               st.session_state.partner_character = session.get("partner_character", "")

        # 删除会话信息
        with HisButton2:
           if st.button("",width="stretch",icon="❌️",key=f"delete_{session['ConTime']}"):
               if delete_session(session["ConTime"]):
                   st.rerun()


    # 分割线
    st.divider()

    st.subheader("AI 伴侣")

    if st.button("新建会话",width="stretch",icon="✏️"):
        # 保存会话
        save_session()

        # 重置展示内容，标识时间，昵称和性格
        st.session_state.ConMemory = []
        st.session_state.ConTime=TimeID()
        st.session_state.partner_name = ""
        st.session_state.partner_character = ""

        # 创建新的会话
        save_session()
        # 强制刷新页面
        st.rerun()
        

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

for record in st.session_state.ConMemory:
    st.chat_message(record["role"]).write(record["content"])

prompt = st.chat_input("请输入您要问的问题？")
if prompt is not None:
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

    st.session_state.ConMemory.append({"role": "assistant", "content": full_response})
 