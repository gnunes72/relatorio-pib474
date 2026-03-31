import streamlit as st
from datetime import date
import pandas as pd
from io import BytesIO
import urllib.parse
from PIL import Image
import os

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="PIB Floripa - Relatório", page_icon="⛪", layout="centered")

# --- DESIGN E ESTILIZAÇÃO CSS AVANÇADA ---
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    
    /* Cabeçalho */
    .pib-header-title { color: #004d40; font-size: 40px !important; font-weight: 800; text-align: center; margin-bottom: 0px; }
    .pib-header-subtitle { color: #004d40; font-size: 18px !important; text-align: center; margin-top: -10px; }
    
    /* Faixas de Subtítulos */
    .pib-faixa {
        background-color: #004d40;
        color: #ffffff !important;
        padding: 8px 15px;
        border-radius: 6px;
        font-size: 15px !important;
        font-weight: 600;
        margin-top: 15px;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .pib-faixa-center { justify-content: center; }

    /* Estilo dos Containers (Fundo mais escuro para contraste) */
    .stExpander { 
        border: 1px solid #81c784; 
        border-radius: 12px; 
        background-color: #dae9db !important; /* Tom mais escuro para contraste */
        margin-bottom: 15px; 
    }
    
    /* Input Fields Brancos para Contraste Máximo */
    .stNumberInput div div input, .stTextInput div div input { 
        background-color: #ffffff !important; 
        border-radius: 8px !important;
    }
    
    /* Botão WhatsApp Redondo/Ícone */
    .btn-wa-circle {
        background-color: #25D366;
        color: white !important;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        text-decoration: none;
        transition: 0.3s;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    }
    .btn-wa-circle:hover { transform: scale(1.1); background-color: #128C7E; }

    label { color: #004d40 !important; font-weight: 700 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- SISTEMA DE ACESSO ---
if st.sidebar.text_input("🔐 Senha:", type="password").upper() == "PIB474":
    
    # --- LOGO E TÍTULOS ---
    col_l, col_t = st.columns([1, 3.5])
    with col_l:
        if os.path.exists("logo.png"): st.image("logo.png", width=110)
    with col_t:
        st.markdown('<p class="pib-header-title">PIB FLORIPA</p>', unsafe_allow_html=True)
        st.markdown('<p class="pib-header-subtitle">Primeira Igreja Batista de Florianópolis</p>', unsafe_allow_html=True)

    # --- CULTO 09:00 ---
    with st.expander("⛪ CULTO DAS 09:00h", expanded=True):
        r9 = st.text_input("Responsável (9h)", key="r9")
        d9 = st.date_input("Data (9h)", value=None, format="DD/MM/YYYY", key="d9")
        
        st.markdown('<div class="pib-faixa pib-faixa-center">Compareceram</div>', unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        t9 = c1.number_input("Templo", min_value=0, key="t9_n")
        v9 = c2.number_input("Visitantes", min_value=0, key="v9_n")
        s9 = c3.number_input("6º Andar", min_value=0, key="s9_n")
        
        st.markdown('<div class="pib-faixa">🤝 Servindo</div>', unsafe_allow_html=True)
        s1, s2, s3 = st.columns(3)
        di9 = s1.number_input("Diaconia", min_value=0, key="di9")
        me9 = s2.number_input("Mesa", min_value=0, key="me9")
        lo9 = s3.number_input("Louvor", min_value=0, key="lo9")

        st.markdown('<div class="pib-faixa">🎒 MI (Infantil)</div>', unsafe_allow_html=True)
        mi_c9 = st.number_input("Crianças (MI)", min_value=0, key="mic9")
        
        st.markdown('<div class="pib-faixa">🎮 MPA (Pré-Adolescente)</div>', unsafe_allow_html=True)
        mpa_c9 = st.number_input("Crianças (MPA)", min_value=0, key="mpac9")

    # --- CULTO 11:00 ---
    with st.expander("⛪ CULTO DAS 11:00h", expanded=False):
        r11 = st.text_input("Responsável (11h)", key="r11")
        
        st.markdown('<div class="pib-faixa pib-faixa-center">Compareceram</div>', unsafe_allow_html=True)
        c4, c5, c6 = st.columns(3)
        t11 = c4.number_input("Templo ", min_value=0, key="t11_n")
        v11 = c5.number_input("Visitantes ", min_value=0, key="v11_n")
        s11 = c6.number_input("6º Andar ", min_value=0, key="s11_n")
        
        st.markdown('<div class="pib-faixa">🤝 Servindo</div>', unsafe_allow_html=True)
        di11 = st.number_input("Diaconia ", min_value=0, key="di11")

    # --- CÁLCULOS E RELATÓRIO ---
    total_dia = (t9+v9+s9+di9+me9+lo9+mi_c9+mpa_c9) + (t11+v11+s11+di11)
    d_str = d9.strftime('%d/%m/%Y') if d9 else ""
    
    relatorio = f"Relatório PIB Floripa - {d_str}\nTotal Geral: {total_dia}\n9h: {t9+v9+s9+di9+me9+lo9+mi_c9+mpa_c9}\n11h: {t11+v11+s11+di11}"

    # --- BOTÕES DE SAÍDA ---
    st.markdown("---")
    col_a, col_b, col_c = st.columns([1, 1, 3])
    
    with col_a:
        wa_link = f"https://wa.me/?text={urllib.parse.quote(relatorio)}"
        st.markdown(f'<a href="{wa_link}" target="_blank" class="btn-wa-circle"> WhatsApp </a>', unsafe_allow_html=True)
    
    with col_b:
        df = pd.DataFrame([{"Data": d_str, "Total": total_dia}])
        buf = BytesIO()
        with pd.ExcelWriter(buf, engine='xlsxwriter') as wr: df.to_excel(wr, index=False)
        st.download_button("📥 Planilha", buf.getvalue(), f"pib_{d_str}.xlsx")

    with st.expander("📋 CÓPIA MANUAL"):
        st.code(relatorio)

else:
    st.info("Aguardando senha para liberar o sistema PIB Floripa.")
