# streamlit库，快速基于python代码构建交互式web网站
# 引入streamlit库
# 基础提供的API构建web应用
# 运行程序：streamlit run xxx.py
# 注意保存文件，不然显示错误.(设置自动保存即可)

# 设置别名st
import streamlit as st 

# 标题
st.title("streamlit入门")
st.header("一级标题")
st.subheader("二级标题")

# 段落文本
st.write("这是文本啦啦啦德玛西亚")
# # 显示图片
# st.image("")
# # 显示音频
# st.audio("")
# # 显示视频
# st.video("")
# 显示logo（左上角小图标）
# st.logo("")
# 显示表格
data={"姓名":["张三","李四","王五"],
    "年龄":[18,19,20],
    "性别":["男","女","男"]
      }
st.table(data)

# 输入框
name=st.text_input("请输入姓名")
age=st.number_input("请输入年龄",min_value=0,max_value=120,step =1)
st.write(f"姓名：{name}，年龄：{age}")
# 密码输入框
password=st.text_input("请输入密码",type="password")
st.write(f"密码：{password}")
# 单选按钮
gender=st.radio("请选择性别",["男","女"])
st.write(f"性别：{gender}")
# 多选框
hobby=st.multiselect("请选择爱好",["篮球","足球","游泳"])
st.write(f"爱好：{hobby}")
# 下拉框
city=st.selectbox("请选择城市",["北京","上海","广州"])
st.write(f"城市：{city}")

# 简而言之，前端的交互式组件（输入框、按钮等）可以通过streamlit的API轻松实现，而不需要编写复杂的HTML、CSS和JavaScript代码。streamlit会自动处理这些组件的渲染和交互逻辑，使得开发者能够专注于业务逻辑的实现。

# 页面配置
st.set_page_config(
    page_title="我的streamlit应用",  # 网页标题
    page_icon=":smiley:",           # 网页图标，可以是emoji或者图片路径，也可以是URL，只是网页标题最前端的图标
    layout="wide",                  # 页面布局
    initial_sidebar_state="expanded",# 侧边栏默认状态
    # menu_items={
    #     'Get help': 'https://www.taobao.com',
    #     'Report a bug': 'https://www.ollama.com',
    #     'About': "这是一个使用streamlit构建的简单应用。"
    # }
    # # menu_items 字典固定这三个键，分别是 'Get help'、'Report a bug' 和 'About'，
    # # 对应的可以是别的链接或信息
)