import streamlit as st
from crew import crew
from fpdf import FPDF
import io

st.set_page_config(page_title="Agentic AI Blog Generator", page_icon="📝")

st.title("📝 Agentic AI Blog Generator")
st.write("Enter a topic below, and the AI will research and generate a blog post for you.")

topic = st.text_input("Topic", placeholder="e.g., Artificial Intelligence trends")

def text_to_pdf(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    # Split text by lines and add them
    for line in text.split('\n'):
        pdf.multi_cell(0, 10, line)
    pdf_output = io.BytesIO()
    pdf.output(pdf_output)
    return pdf_output.getvalue()

if st.button("Generate Blog"):
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

            # Provide download button for Markdown
            filename_md = f"blog_post_{topic.replace(' ', '_')}.md"
            st.download_button(
                label="Download as Markdown",
                data=blog_content,
                file_name=filename_md,
                mime="text/markdown",
            )

            # Provide download button for PDF
            pdf_data = text_to_pdf(blog_content)
            filename_pdf = f"blog_post_{topic.replace(' ', '_')}.pdf"
            st.download_button(
                label="Download as PDF",
                data=pdf_data,
                file_name=filename_pdf,
                mime="application/pdf",
            )
        else:
            st.warning("No blog content generated. Try again with a different topic.")
