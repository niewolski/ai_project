import streamlit as st
import os
from process_data import extract_text_from_pdf, extract_text_from_docx, extract_data_from_xlsx
from ai_chat import generate_response

# Konfiguracja strony
st.set_page_config(page_title="Pomocnik dla PATRZ GLOBALNIE", layout="centered")

# Ścieżka do logo
logo_path = os.path.join(os.path.dirname(__file__), "logo.png")

# Sprawdzenie czy plik istnieje
if os.path.exists(logo_path):
    st.image(logo_path, width=100)
else:
    st.warning("⚠️ Logo nie zostało znalezione!")

# Nagłówek
st.markdown("<p class='title'>Pomocnik dla PATRZ GLOBALNIE</p>", unsafe_allow_html=True)

# Pole na pytanie
st.write("### O co chcesz zapytać?")
query = st.text_input("")

# Przycisk do wyszukiwania odpowiedzi
if st.button("Znajdź odpowiedź"):
    if query:
        response = generate_response(query)
        st.write("### Odpowiedź:")
        st.write(response)
    else:
        st.warning("Proszę wpisać pytanie.")
