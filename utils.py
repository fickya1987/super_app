import streamlit as st

def about():
    about_text = """Aplikasi Streamlit berbasis AI ini memungkinkan pengguna untuk berinteraksi dengan berbagai LLM (Large Language Models) melalui berbagai jenis media input, termasuk teks, gambar, audio, suara, video, PDF, Docx, dan tautan. Pengguna dapat memilih antara model Chatbot, Agen, atau Ringkasan, menyesuaikan respons suara, dan mengatur ulang percakapan sesuai kebutuhan. Aplikasi ini memproses dan merespons pertanyaan secara real-time, memberikan pengalaman yang intuitif dan serbaguna."""
    return about_text


def set_safety_settings():
    safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE"
    },
]

    return safety_settings
