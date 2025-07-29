import streamlit as st
from PIL import Image
import io

st.set_page_config(page_title="Multimodal RAG Assistant", layout="wide")
st.title("📘 Multimodal RAG Research Paper Assistant")

# --- Upload section ---
uploaded_pdf = st.file_uploader("Upload a research paper (PDF)", type=["pdf"])

rag_mode = st.sidebar.radio(
    "Choose extraction mode:",
    ["Text only", "Text + Tables", "Full (Text + Tables + Images)"]
)

# --- Mock Logic for Testing ---
def mock_parse_pdf(file, mode):
    return {"text": "Sample text from PDF", "images": [], "tables": []}

def mock_answer_question(question, docs, mode):
    dummy_answer = f"Mocked answer for: '{question}'"
    dummy_sources = [{"page": 1}, {"page": 3}]
    dummy_images = [Image.new("RGB", (300, 200), color="lightblue")]
    return dummy_answer, dummy_sources, dummy_images

# --- Display + Parse section ---
if uploaded_pdf:
    with st.spinner("Parsing PDF..."):
        parsed_docs = mock_parse_pdf(uploaded_pdf, mode=rag_mode)
    st.success("✅ PDF parsed successfully.")

    st.subheader("Ask a question about the paper:")
    question = st.text_input("❓ Your question", placeholder="e.g. What is the main contribution?")

    if st.button("🔍 Generate Answer") and question:
        with st.spinner("Generating answer..."):
            answer, sources, visuals = mock_answer_question(question, parsed_docs, rag_mode)

        st.markdown("### 🧠 Answer")
        st.markdown(answer)

        if visuals:
            st.markdown("### 📊 Visual Results")
            for img in visuals:
                st.image(img, caption="Example visual", use_column_width=True)

        if sources:
            st.markdown("### 📄 Sources")
            for i, source in enumerate(sources, 1):
                st.markdown(f"{i}. Page {source.get('page', '?')}")
else:
    st.info("📥 Please upload a research paper in PDF format.")
