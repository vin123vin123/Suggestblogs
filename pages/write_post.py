from db import create_post
import streamlit as st

st.header("✍️ Write a New Post")

with st.form("new_post_form", clear_on_submit=True):
    title = st.text_input("Title")
    author = st.text_input("Author")
    content = st.text_area("Content", height=220)

    uploaded_file = st.file_uploader(
        "Upload a cover image (optional, max 15MB)",
        type=["jpg", "jpeg", "png"],
    )

    submitted = st.form_submit_button("Publish Post", type="primary")

    if submitted:
        if not (title.strip() and author.strip() and content.strip()):
            st.error("Please fill in Title, Author, and Content.")
        else:
            try:
                image_bytes = None
                image_type = None

                if uploaded_file is not None:
                    image_bytes = uploaded_file.getvalue()
                    image_type = uploaded_file.type

                create_post(
                    title.strip(),
                    author.strip(),
                    content.strip(),
                    image_bytes,
                    image_type,
                )
                st.success("✅ Post published! Switch to 'Read Posts' to view it.")
            except Exception as e:
                st.error(f"Database Upload Error: {e}")
