import streamlit as st
from datetime import date
import pandas as pd
from io import BytesIO
import urllib.parse
from PIL import Image
import os

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="PIB Floripa - Gestão", page_icon="⛪", layout="centered")

# --- ESTILIZAÇÃO CSS PROFISSIONAL ---
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    
    /* Cabeçalho */
    .pib-header-title { color: #004d40; font-size: 38px !important; font-weight: 800; text-align: center; margin-bottom: 0px; }
    .pib-header-subtitle { color: #004d40; font-size: 17px !important; text-align: center; margin-top: -10px; margin-bottom: 25px; }
    
    /* Faixas de Subtítulos */
    .pib-faixa {
        background-color: #004d40;
        color: #ffffff !important;
        padding: 8px 15px;
        border-radius: 6px;
        font-size: 14px !important;
        font-weight: 600;
        margin-top: 15px;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .pib-faixa-center { justify-content: center; text-transform: uppercase; letter-spacing: 1px; }

    /* Containers (Contraste de Fundo) */
    .stExpander { 
        border: 1px solid #81c784; 
        border-radius: 12px; 
        background-color: #e3eedf !important; /* Tom escurecido para contraste */
        margin-bottom: 15px; 
    }
    
    /* Campos de Entrada Brancos */
    .stNumberInput div div input, .stTextInput div div input { 
        background-color: #ffffff !important; 
        border-radius: 8px !important;
    }
    
    /* Padronização dos Botões de Ação */
    .pib-btn-container { display: flex; gap: 10px; justify-content: space-between; margin-top: 20px; }
    
    .stButton>button {
        background-color: #004d40 !important;
        color: white !important;
        height: 45px !important;
        width: 100% !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        border: none !important;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
    }
    
    .btn-link-wa {
        text-decoration: none !important;
        background-color: #004d40;
        color: white !important;
        height: 45px;
        width: 100%;
        border-radius: 8px;
        font-weight: bold;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
        font-size: 14px;
    }

    label { color: #004d40 !important; font-weight: 700 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- SENHA (MAIÚSCULA/MINÚSCULA) ---
if st.sidebar.text_input("🔐 Acesso:", type="password").upper() == "PIB474":
    
    # --- LOGO E TÍTULOS ---
    col_l, col_t = st.columns([1, 4])
    with col_l:
        if os.path.exists("logo.png"): st.image("logo.png", width=100)
    with col_t:
        st.markdown('<p class="pib-header-
