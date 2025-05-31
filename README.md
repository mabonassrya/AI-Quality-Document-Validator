# 📄 AI Quality Document Validator

This is a Streamlit-based web application that allows construction professionals to validate quality documents (e.g., concrete mix designs, test reports) against project specifications using GPT-4o.

## 🚀 Features

- ✅ Upload and extract text from PDF or DOCX specification files  
- ✅ Upload corresponding quality documents  
- ✅ Automatically extract key requirements using OpenAI GPT-4o  
- ✅ Validate whether each requirement is Met, Partially Met, or Missing  
- ✅ Generate a clean summary highlighting compliance gaps  
- ✅ API key management via `.env.txt` file  
- ✅ Fully local or deployable via Streamlit Cloud  

## 📂 File Structure

```
├── app.py               # Main Streamlit application  
├── .env.txt             # File containing your OpenAI API key (OPENAI_API_KEY)  
├── requirements.txt     # Dependencies for deployment  
└── README.md            # This file  
```

## 🧪 Technologies

- [Streamlit](https://streamlit.io/)  
- [OpenAI GPT-4o API](https://platform.openai.com/docs/models/gpt-4o)  
- [PyPDF2](https://pypi.org/project/PyPDF2/)  
- [python-docx](https://python-docx.readthedocs.io/)  
- [dotenv](https://pypi.org/project/python-dotenv/)  

## 📦 Setup Instructions

1. **Clone the repository**  
   ```bash
   git clone https://github.com/mabonassrya/AI-Quality-Document-Validator.git  
   cd AI-Quality-Document-Validator  
   ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt  
   ```

3. **Create a `.env.txt` file** in the project root and add your OpenAI API key:  
   ```txt
   OPENAI_API_KEY=sk-...  
   ```

4. **Run the app locally**  
   ```bash
   streamlit run app.py  
   ```

5. **Deploy on [Streamlit Cloud](https://streamlit.io/cloud)**  
   - Link your GitHub repo  
   - Set `app.py` as the main file  
   - Add a secret called `OPENAI_API_KEY` under the `Secrets` tab  

## ✅ Example Use Case

- Upload: `610.07.docx` (specification)  
- Upload: `Mix1.pdf` (quality document)  
- Output: Lists requirement validation statuses and generates a summary  

## 📄 License

This project is licensed under the [MIT License](LICENSE).  

## 📬 Contact

For feedback, suggestions, or inquiries:

**Maitham Abonassrya**  
📧 [maitham_k79@yahoo.com](mailto:maitham_k79@yahoo.com)  
