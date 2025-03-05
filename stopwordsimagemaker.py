import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords
import string

# Download stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def process_text(text):
    # Remove punctuation and stopwords
    words = text.translate(str.maketrans('', '', string.punctuation)).split()
    filtered_words = [word.lower() for word in words if word.lower() not in stop_words]
    return " ".join(filtered_words)

def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    return wordcloud

# Streamlit UI
st.title("Stopwords Image Maker")

uploaded_file = st.file_uploader("Upload a text file", type=["txt"])

if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")
    
    st.subheader("Original Text")
    st.text_area("", text, height=200)
    
    processed_text = process_text(text)
    st.subheader("Processed Text (Without Stopwords)")
    st.text_area("", processed_text, height=200)
    
    if st.button("Generate Word Cloud"):
        wordcloud = generate_wordcloud(processed_text)
        
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.imshow(wordcloud, interpolation="bilinear")
        ax.axis("off")
        st.pyplot(fig)