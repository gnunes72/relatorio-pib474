import streamlit as st
from datetime import date
import pandas as pd
from io import BytesIO
import urllib.parse
from PIL import Image
import os

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="PIB Floripa - Gestão", page_icon="⛪", layout="centered")

# --- ESTILIZAÇÃO CSS (FOCO EM SIMETRIA E PADRONIZAÇÃO) ---
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    
    /* Cabeçalho Profissional */
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

    /* Containers com fundo escurecido para contraste */
    .stExpander { 
        border: 1px solid #81c784; 
        border-radius: 12px; 
        background-color: #e3eedf !important; 
        margin-bottom: 15px; 
    }
    
    /* Campos de Entrada Brancos */
    .stNumberInput div div input, .stTextInput div div input { 
        background-color: #ffffff !important; 
        border-radius: 8px !important;
    }
    
    /* Layout dos Botões em Linha com Ícones Externos */
    .action-container {
        display: flex;
        justify-content: space-between;
        align-items: flex-end;
        margin-top: 30px;
        text-align: center;
    }
    
    .action-item {
        flex: 1;
        display: flex;
        flex-direction: column;
        align-items: center;
        max-width: 30%; /* Garante que os 3 caibam na linha */
    }

    .icon-label {
        font-size: 24px;
        margin-bottom: 5px;
    }

    /* Botões Padronizados */
    .stButton>button, .btn-wa-custom {
        background-color: #004d40 !important;
        color: white !important;
        height: 45px !important;
        width: 100% !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        border: none !important;
        font-size: 14px !important;
        display: flex;
        align-items: center;
        justify-content: center;
        text-decoration: none !important;
    }

    label { color: #004d40 !important; font-weight: 700 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- LOGIN ---
if st.sidebar.text_input("🔐 Acesso:", type="password").upper() == "PIB474":
    
    # --- LOGO E TÍTULOS ---
    col_l, col_t = st.columns([1, 4])
    with col_l:
        if os.path.exists("logo.png"): st.image("logo.png", width=100)
    with col_t:
        st.markdown('<p class="pib-header-title">PIB FLORIPA</p>', unsafe_allow_html=True)
        st.markdown('<p class="pib-header-subtitle">Primeira Igreja Batista de Florianópolis</p>', unsafe_allow_html=True)

    # --- FORMULÁRIO 09:00 (Fundo escurecido conforme solicitado) ---
    with st.expander("⛪ CULTO DAS 09:00h", expanded=True):
        r9 = st.text_input("Responsável (9h)", key="r9")
        d9 = st.date_input("Data (9h)", value=None, format="DD/MM/YYYY", key="d9")
        
        st.markdown('<div class="pib-faixa pib-faixa-center">Compareceram</div>', unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        t9 = c1.number_input("Templo", min_value=0, key="t9n")
        v9 = c2.number_input("Visitantes", min_value=0, key="v9n")
        s9 = c3.number_input("6º Andar", min_value=0, key="s9n")
        
        st.markdown('<div class="pib-faixa">🤝 Servindo</div>', unsafe_allow_html=True)
        s1, s2, s3 = st.columns(3)
        di9 = s1.number_input("Diaconia", min_value=0, key="di9")
        me9 = s2.number_input("Mesa", min_value=0, key="me9")
        lo9 = s3.number_input("Louvor", min_value=0, key="lo9")

        st.markdown('<div class="pib-faixa">🎒 MI (Infantil)</div>', unsafe_allow_html=True)
        mi9 = st.number_input("Crianças (MI)", min_value=0, key="mi9n")
        
        st.markdown('<div class="pib-faixa">🎮 MPA (Pré-Adolescente)</div>', unsafe_allow_html=True)
        mpa9 = st.number_input("Crianças (MPA)", min_value=0, key="mpa9n")

    # --- PROCESSAMENTO ---
    d_str = d9.strftime('%d/%m/%Y') if d9 else ""
    tot9 = (t9+v9+s9+di9+me9+lo9+mi9+mpa9)
    relatorio = f"Relatório PIB Floripa - {d_str}\n\nTotal Culto 9h: {tot9} pessoas."

    # --- SEÇÃO DE AÇÕES (PADRONIZADA E EM ORDEM ALFABÉTICA) ---
    st.markdown("---")
    
    # Criamos a estrutura de colunas para os botões
    col_p, col_t, col_w = st.columns(3)

    # 1. PLANILHA (P)
    with col_p:
        st.markdown('<div style="text-align: center;"><span class="icon-label">📥</span></div>', unsafe_allow_html=True)
        df = pd.DataFrame([{"Data": d_str, "Total": tot9}])
        buf = BytesIO()
        with pd.ExcelWriter(buf, engine='xlsxwriter') as wr: df.to_excel(wr, index=False)
        st.download_button("PLANILHA", buf.getvalue(), f"pib_{d_str}.xlsx")

    # 2. TEXTO (T) - Centralizado
    with col_t:
        st.markdown('<div style="text-align: center;"><span class="icon-label">📋</span></div>', unsafe_allow_html=True)
        show_text = st.button("TEXTO")

    # 3. WHATSAPP (W)
    with col_w:
        st.markdown('<div style="text-align: center;"><span class="icon-label">📲</span></div>', unsafe_allow_html=True)
        link_wa = f"https://wa.me/?text={urllib.parse.quote(relatorio)}"
        st.markdown(f'<a href="{link_wa}" target="_blank" class="btn-wa-custom">WHATSAPP</a>', unsafe_allow_html=True)

    if show_text:
        st.code(relatorio)

else:
    st.info("Insira a senha para acessar.")
