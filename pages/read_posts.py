from db import get_all_posts
import streamlit as st

st.header("📖 Read Posts")

col1, col2 = st.columns([4, 1])
with col1:
    search_query = st.text_input(
        "Search by title or author",
        placeholder="Type to filter posts...",
        label_visibility="collapsed",
    )
with col2:
    if st.button("🔄 Refresh", use_container_width=True):
        get_all_posts.clear()
        st.rerun()

try:
    posts = get_all_posts()

    if search_query:
        q = search_query.lower()
        posts = [
            p
            for p in posts
            if q in p.get("title", "").lower()
            or q in p.get("author", "").lower()
        ]

    if not posts:
        st.info("No posts found.")
    else:
        for post in posts:
            with st.expander(f"**{post['title']}** — by {post['author']}"):
                if post.get("image"):
                    st.image(bytes(post["image"]), use_container_width=True)
                st.write(post["content"])
                st.caption(f"Published: {post.get('created_at', '')}")

except Exception as e:
    st.error(f"Could not load posts from MongoDB: {e}")
