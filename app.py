import streamlit as st
from txtai.pipeline import Summary
from PyPDF2 import PdfFileReader
from rouge_score import rouge_scorer

st.set_page_config(layout='wide')

def calculate_rouge(generated_summary, reference_summary):
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    scores = scorer.score(generated_summary, reference_summary)
    return scores

@st.cache_resource
def summary_text(text):
    summary = Summary()
    text = (text)
    result = summary(text)
    return result

# Extract text from the PDF file using pyPDF2
def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as f:
        reader = PdfFileReader(f)
        page = reader.pages[0]
        text = page.extract_text()
    return text

choice = st.sidebar.selectbox('select your choice', ['Summarize Text', 'Summarize Document'])

if choice == 'Summarize Text':
    st.title('_SummarizeME_ is :blue[cool] :sunglasses:')
    st.text('Ini adalah website _text summary_  yang dapat memudahkan dalam merangkum sebuah kalimat.')
    st.text('Project ini disusun oleh: Muhammad Reski Djunaedi, Muhammad Rofiul Arham, Syayid Muhammad Akbar, Sintia Sari, Reva Aulia Faradilah')
    input_text = st.text_area('Enter your text here !')
    if input_text is not None:
        if st.button('Summarize Text'):
            col1, col2 = st.columns([1,1])
            with col1:
                st.markdown("***your input text***")
                st.info(input_text)
            with col2:
                result = summary_text(input_text)
                st.markdown("***Summary***")
                st.success(result)\
                
                # Add reference summary for ROUGE evaluation
                reference_summary = (input_text)        
