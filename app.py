# ✅ Streamlit App: AI-Based Quality Document Validator (GPT-4o)

import streamlit as st
import openai
from PyPDF2 import PdfReader
from docx import Document
import tempfile
from dotenv import load_dotenv
import os

# ----------------------------
# Load API Key from .env
# ----------------------------
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# ----------------------------
# Page config
# ----------------------------
st.set_page_config(page_title="AI Quality Validator", layout="centered")
st.title("📄 AI Quality Document Validator")
st.markdown("Validate construction quality documents against specifications using GPT-4o.")

# ----------------------------
# Upload Files
# ----------------------------
spec_file = st.file_uploader("📑 Upload Specification File (.pdf or .docx)", type=["pdf", "docx"])
doc_file = st.file_uploader("📋 Upload Quality Document (.pdf or .docx)", type=["pdf", "docx"])

# ----------------------------
# Helper Functions
# ----------------------------
def extract_text_from_pdf(file):
    reader = PdfReader(file)
    return "".join([page.extract_text() for page in reader.pages if page.extract_text()])

def extract_text_from_docx(file):
    doc = Document(file)
    return "\n".join([p.text for p in doc.paragraphs])

def extract_requirements_from_spec(text):
    prompt = """
You are reviewing a construction specification.
Some paragraphs contain general requirements followed by specific sub-items (e.g., “Evidence shall be provided within 12 months, including: compressive strength, drying shrinkage...”)
Your task is to extract all requirements clearly and separately:
1. The general (parent) requirement.
2. Each sub-requirement as a separate item.
Output each as its own line.
Now extract all such requirements from the following specification:
"""
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an expert in construction specification extraction."},
            {"role": "user", "content": prompt + text}
        ],
        temperature=0,
        max_tokens=4000,
        api_key=openai_api_key
    )
    return response.choices[0].message.content.strip()

def validate_document_against_requirements(doc_text, requirements_text):
    prompt = f"""
The following is the content of a construction quality document:
{doc_text}

Validate against the following requirements:
{requirements_text}

For each requirement, state whether it is Met / Partially Met / Missing.
Summarize only the missing and partially met ones at the end.
"""
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an expert in construction compliance validation."},
            {"role": "user", "content": prompt}
        ],
        temperature=0,
        max_tokens=4000,
        api_key=openai_api_key
    )
    return response.choices[0].message.content.strip()

# ----------------------------
# Run validation
# ----------------------------
if st.button("✅ Run Validation"):
    if not openai_api_key:
        st.error("❌ API key is missing. Please set it in your .env file.")
    elif not spec_file or not doc_file:
        st.warning("⚠️ Please upload both the specification and the document.")
    else:
        try:
            with st.spinner("🔍 Extracting and validating..."):
                spec_text = extract_text_from_docx(spec_file) if spec_file.name.endswith(".docx") else extract_text_from_pdf(spec_file)
                doc_text = extract_text_from_docx(doc_file) if doc_file.name.endswith(".docx") else extract_text_from_pdf(doc_file)
                requirements = extract_requirements_from_spec(spec_text)
                validation_result = validate_document_against_requirements(doc_text, requirements)
                st.success("✅ Validation Complete")
                st.markdown("### 📊 Result:")
                st.text_area("Validation Output", validation_result, height=400)
        except Exception as e:
            st.error(f"An error occurred: {e}")
