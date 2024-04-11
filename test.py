import streamlit as st
from transformers import pipeline, AutoTokenizer

# Загрузка модели и токенизатора для машинного перевода
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-ru-en")
tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-ru-en")

# Стартовая страница Streamlit
st.title("Перевод текста с русского на английский")

# Элемент управления для ввода текста
user_text = st.text_area("Введите текст:")

# Элемент управления для машинного перевода
if st.button("Перевести текст"):
    translated_text = translator(user_text)[0].get('translation_text')
    st.write(f"Результат перевода: {translated_text}")

