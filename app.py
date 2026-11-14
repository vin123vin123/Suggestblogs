import streamlit as st

st.set_page_config(page_title="My Blog", page_icon="📝", layout="centered")
st.title("📝 My Blog")

read_page = st.Page("pages/read_posts.py", title="Read Posts", icon="📖")
write_page = st.Page("pages/write_post.py", title="Write a Post", icon="✍️")

pg = st.navigation([read_page, write_page])
pg.run()
