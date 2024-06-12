import streamlit as st
from txtai.pipeline import Summary
from PyPDF2 import PdfReader

# Set page configuration
st.set_page_config(layout='wide')

# Function to summarize text
@st.cache_resource
def summary_text(text):
    summary = Summary()
    result = summary(text)
    return result

# Extract text from the PDF file using PyPDF2
def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        extracted_text = page.extract_text()
        if extracted_text:
            text += extracted_text
    return text

# Sidebar choice
choice = st.sidebar.selectbox('Select your choice', ['Summarize Text', 'Summarize Document'])

if choice == 'Summarize Text':
    st.title('_SummarizeME_ is :blue[cool] :sunglasses:')
    st.text('Ini adalah website _text summary_ yang dapat memudahkan dalam merangkum sebuah kalimat.')
    st.text('Project ini disusun oleh: Muhammad Reski Djunaedi, Muhammad Rofiul Arham, Syayid Muhammad Akbar, Sintia Sari, Reva Aulia Faradilah')
    input_text = st.text_area('Enter your text here!')
    if input_text:
        if st.button('Summarize Text'):
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("***Your Input Text***")
                st.info(input_text)
            with col2:
                result = summary_text(input_text)
                st.markdown("***Summary***")
                st.success(result)
                # Add reference summary for ROUGE evaluation
                reference_summary = input_text

elif choice == 'Summarize Document':
    st.title('Summarize Document')
    st.text('Unggah dokumen PDF Anda untuk diringkas.')
    uploaded_file = st.file_uploader('Choose a PDF file', type='pdf')
    if uploaded_file is not None:
        text = extract_text_from_pdf(uploaded_file)
        if text:
            st.markdown("***Extracted Text from PDF***")
            st.info(text)

            result = summary_text(text)
            st.markdown("***Summary***")
            st.success(result)
        else:
            st.error("Could not extract text from the uploaded PDF.")
