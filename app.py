import streamlit as st
from crew import crew
import sys
import pysqlite3
sys.modules["sqlite3"] = pysqlite3

st.set_page_config(page_title="Agentic AI Blog Generator", page_icon="📝")

st.title("📝 Agentic AI Blog Generator")
st.write("Enter a topic below, and the AI will research and generate a blog post for you.")

with st.form(key="blog_form"):
    topic = st.text_input("Topic", placeholder="e.g., Artificial Intelligence trends")
    submit_button = st.form_submit_button(label="Generate Blog")

if submit_button:
    if not topic.strip():
        st.warning("Please enter a valid topic!")
    else:
        with st.spinner("Generating blog... Please wait."):
            result = crew.kickoff(inputs={"topic": topic})

            blog_content = ""
            if isinstance(result, dict):
                blog_content = result.get("output") or result.get("result") or str(result)
            else:
                blog_content = str(result)

        if blog_content:
            st.success("Blog generated successfully!")
            st.markdown("### Generated Blog Content")
            st.markdown(blog_content)

            filename_md = f"blog_post_{topic.replace(' ', '_').lower()}.md"
            st.download_button(
                label="Download as Markdown",
                data=blog_content,
                file_name=filename_md,
                mime="text/markdown",
            )
        else:
            st.warning("No blog content generated. Try again with a different topic.")
