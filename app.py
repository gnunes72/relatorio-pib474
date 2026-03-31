import streamlit as st
from datetime import date
import pandas as pd
from io import BytesIO
import urllib.parse
from PIL import Image
import os

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="PIB Floripa", page_icon="⛪", layout="centered")

# --- ESTILIZAÇÃO CSS (FOCO EM PADRONIZAÇÃO RÍGIDA) ---
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    
    .pib-header-title { color: #004d40; font-size: 38px !important; font-weight: 800; text-align: center; margin-bottom: 0px; }
    .pib-header-subtitle { color: #004d40; font-size: 17px !important; text-align: center; margin-top: -10px; margin-bottom: 25px; }
    
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
    .pib-faixa-center { justify-content: center; text-transform: uppercase; }

    .stExpander { 
        border: 1px solid #81c784; 
        border-radius: 12px; 
        background-color: #e3eedf !important; 
        margin-bottom: 15px; 
    }
    
    .stNumberInput div div input, .stTextInput div div input { 
        background-color: #ffffff !important; 
        border-radius: 8px !important;
    }
    
    /* BOTÕES PADRONIZADOS: MESMA COR, ALTURA E FONTE */
    .stButton>button, .btn-pib-link {
        background-color: #004d40 !important;
        color: white !important;
        height: 50px !important;
        width: 100% !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        font-size: 14px !important; /* Mesma fonte do MI/MPA */
        border: none !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        gap: 8px !important;
        text-decoration: none !important;
    }

    label { color: #004d40 !important; font-weight: 700 !important; }
    </style>
    """, unsafe_allow_html=True)

if st.sidebar.text_input("🔐 Acesso:", type="password").upper() == "PIB474":
    
    col_l, col_t = st.columns([1, 4])
    with col_l:
        if os.path.exists("logo.png"): st.image("logo.png", width=100)
    with col_t:
        st.markdown('<p class="pib-header-title">PIB FLORIPA</p>', unsafe_allow_html=True)
        st.markdown('<p class="pib-header-subtitle">Primeira Igreja Batista de Florianópolis</p>', unsafe_allow_html=True)

    with st.expander("⛪ CULTO DAS 09:00h", expanded=True):
        r9 = st.text_input("Responsável (9h)", key="r9")
        d9 = st.date_input("Data (9h)", value=None, format="DD/MM/YYYY", key="d9")
        
        st.markdown('<div class="pib-faixa pib-faixa-center">Compareceram</div>', unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        t9 = c1.number_input("Templo", min_value=0, key="t9n")
        v9 = c2.number_input("Visitantes", min_value=0, key="v9n")
        s9 = c3.number_input("6º Andar", min_value=0, key="s9n")
        
        st.markdown('<div class="pib-faixa">🤝 Servindo</div>', unsafe_allow_html=True)
        s_col1, s_col2, s_col3 = st.columns(3)
        di9 = s_col1.number_input("Diaconia", min_value=0, key="di9")
        me9 = s_col2.number_input("Mesa", min_value=0, key="me9")
        lo9 = s_col3.number_input("Louvor", min_value=0, key="lo9")

        st.markdown('<div class="pib-faixa">🎒 MI (Infantil)</div>', unsafe_allow_html=True)
        mi9 = st.number_input("Crianças (MI)", min_value=0, key="mi9n")
        
        st.markdown('<div class="pib-faixa">🎮 MPA (Pré-Adolescente)</div>', unsafe_allow_html=True)
        mpa9 = st.number_input("Crianças (MPA)", min_value=0, key="mpa9n")

    # --- PROCESSAMENTO ---
    d_str = d9.strftime('%d/%m/%Y') if d9 else ""
    tot9 = (t9+v9+s9+di9+me9+lo9+mi9+mpa9)
    relatorio = f"Relatório PIB Floripa - {d_str}\nTotal Culto 9h: {tot9} pessoas."

    # --- LINHA DE AÇÕES (PADRONIZADA, ALFABÉTICA, SIMÉTRICA) ---
    st.markdown("---")
    col_arq, col_pla, col_wha = st.columns(3)

    with col_arq:
        show_text = st.button("📄 Arquivo em Texto")

    with col_pla:
        df = pd.DataFrame([{"Data": d_str, "Total": tot9}])
        buf = BytesIO()
        with pd.ExcelWriter(buf, engine='xlsxwriter') as wr: df.to_excel(wr, index=False)
        st.download_button("📊 Planilha", buf.getvalue(), f"pib_{d_str}.xlsx")

    with col_wha:
        link_wa = f"https://wa.me/?text={urllib.parse.quote(relatorio)}"
        st.markdown(f'<a href="{link_wa}" target="_blank" class="btn-pib-link">📲 WhatsApp</a>', unsafe_allow_html=True)

    if show_text:
        st.code(relatorio)

else:
    st.info("Insira a senha para acessar.")
