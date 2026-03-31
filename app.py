import streamlit as st
from datetime import date
import pandas as pd
from io import BytesIO
import urllib.parse
from PIL import Image
import os

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Relatório PIB Floripa", page_icon="⛪", layout="centered")

# --- DESIGN E ESTILIZAÇÃO CSS PROFISSIONAL ---
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    
    /* Cabeçalho Principal */
    .pib-header-title { color: #004d40; font-size: 42px !important; font-weight: 800; margin-bottom: 0px; text-align: center; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    .pib-header-subtitle { color: #004d40; font-size: 19px !important; font-weight: 400; margin-top: -10px; margin-bottom: 5px; text-align: center; }
    .pib-rel-title { color: #2e7d32; font-size: 15px !important; text-align: center; font-weight: bold; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 25px; }
    
    /* Subtítulos com Faixa Verde Escuro e Texto Branco */
    .pib-faixa {
        background-color: #004d40;
        color: #ffffff !important;
        padding: 6px 15px;
        border-radius: 4px;
        font-size: 15px !important;
        font-weight: 600;
        margin-top: 20px;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
        gap: 10px;
        box-shadow: 0px 2px 4px rgba(0,0,0,0.1);
    }

    /* Containers de Entrada (Verde Claríssimo) */
    .stExpander { border: 1px solid #a5d6a7; border-radius: 10px; background-color: #f1f8e9; margin-bottom: 15px; }
    
    /* Labels e Inputs */
    label { color: #004d40 !important; font-weight: 700 !important; font-size: 14px !important; }
    .stNumberInput div div input { background-color: #ffffff !important; }

    /* --- PADRONIZAÇÃO RÍGIDA DOS BOTÕES --- */
    .stButton>button, .btn-pib-custom {
        background-color: #004d40 !important;
        color: white !important;
        height: 50px !important;
        width: 100% !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        font-size: 14px !important; /* Mesma fonte MI/MPA */
        border: none !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        gap: 10px !important;
        text-decoration: none !important;
        transition: 0.3s;
        cursor: pointer;
    }
    .stButton>button:hover, .btn-pib-custom:hover { background-color: #2e7d32 !important; }

    </style>
    """, unsafe_allow_html=True)

# --- SISTEMA DE SENHA ---
senha_usuario = st.sidebar.text_input("🔐 Autenticação:", type="password")

if senha_usuario.upper() == "PIB474":
    
    # --- CABEÇALHO ---
    col_logo, col_nome = st.columns([1, 3.5])
    with col_logo:
        if os.path.exists("logo.png"):
            st.image(Image.open("logo.png"), width=110)
    with col_nome:
        st.markdown('<p class="pib-header-title">PIB FLORIPA</p>', unsafe_allow_html=True)
        st.markdown('<p class="pib-header-subtitle">Primeira Igreja Batista de Florianópolis</p>', unsafe_allow_html=True)
        st.markdown('<p class="pib-rel-title">Relatório de Cultos</p>', unsafe_allow_html=True)
    
    # --- FORMULÁRIO CULTO 09:00 ---
    with st.expander(" 🟢 CULTO DAS 09:00h - Preencher Dados", expanded=True):
        r9 = st.text_input("Responsável pela contagem (9h)", placeholder="Digite o nome...", key="res9")
        d9_input = st.date_input("Data do Culto (9h)", value=None, format="DD/MM/YYYY", key="dat9")
        
        st.markdown('<div class="pib-faixa">👥 Compareceram</div>', unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        t9 = c1.number_input("Templo/Mezanino", min_value=0, key="t9")
        v9 = c2.number_input("Visitantes", min_value=0, key="v9")
        s9 = c3.number_input("Sexto andar", min_value=0, key="s9")
        
        st.markdown('<div class="pib-faixa">🛠️ Servindo</div>', unsafe_allow_html=True)
        s1, s2, s3 = st.columns(3)
        di9 = s1.number_input("Diaconia", min_value=0, key="di9")
        me9 = s2.number_input("Mesa", min_value=0, key="me9")
        lo9 = s3.number_input("Louvor", min_value=0, key="lo9")

        st.markdown('<div class="pib-faixa">🎒 MI (Ministério Infantil)</div>', unsafe_allow_html=True)
        mi1, mi2, mi3 = st.columns(3)
        mic9 = mi1.number_input("Crianças (MI)", min_value=0, key="mic9")
        mis9 = mi2.number_input("Servos (MI)", min_value=0, key="mis9")
        mip9 = mi3.number_input("Pai/Mãe (MI)", min_value=0, key="mip9")

        st.markdown('<div class="pib-faixa">🎮 MPA (Pré-Adolescente)</div>', unsafe_allow_html=True)
        mp1, mp2, mp3 = st.columns(3)
        mpac9 = mp1.number_input("Crianças (MPA)", min_value=0, key="mpac9")
        mpas9 = mp2.number_input("Servos (MPA)", min_value=0, key="mpas9")
        mpap9 = mp3.number_input("Pai/Mãe (MPA)", min_value=0, key="mpap9")
        
        st.markdown('<div class="pib-faixa">📚 Ebed</div>', unsafe_allow_html=True)
        eb9 = st.number_input("Total Ebed", min_value=0, key="eb9", label_visibility="collapsed")

    # --- FORMULÁRIO CULTO 11:00 (PRESERVADO) ---
    with st.expander("🟢 CULTO DAS 11:00h - Preencher Dados", expanded=False):
        r11 = st.text_input("Responsável pela contagem (11h)", placeholder="Digite o nome...", key="res11")
        d11_input = st.date_input("Data do Culto (11h)", value=None, format="DD/MM/YYYY", key="dat11")
        
        st.markdown('<div class="pib-faixa">👥 Compareceram</div>', unsafe_allow_html=True)
        c4, c5, c6 = st.columns(3)
        t11 = c4.number_input("Templo/Mezanino ", min_value=0, key="t11")
        v11 = c5.number_input("Visitantes ", min_value=0, key="v11")
        s11 = c6.number_input("Sexto andar ", min_value=0, key="s11")
        
        st.markdown('<div class="pib-faixa">🛠️ Servindo</div>', unsafe_allow_html=True)
        s4, s5, s6 = st.columns(3)
        di11 = s4.number_input("Diaconia ", min_value=0, key="di11")
        me11 = s5.number_input("Mesa ", min_value=0, key="me11")
        lo11 = s6.number_input("Louvor ", min_value=0, key="lo11")

        st.markdown('<div class="pib-faixa">🎒 MI (Ministério Infantil 11h)</div>', unsafe_allow_html=True)
        mi4, mi5, mi6 = st.columns(3)
        mic11 = mi4.number_input("Crianças (MI 11h)", min_value=0, key="mic11")
        mis11 = mi5.number_input("Servos (MI 11h)", min_value=0, key="mis11")
        mip11 = mi6.number_input("Pai/Mãe (MI 11h)", min_value=0, key="mip11")

        st.markdown('<div class="pib-faixa">🎓 Classe Batismo</div>', unsafe_allow_html=True)
        ba1, ba2, ba3 = st.columns(3)
        bj = ba1.number_input("Jovens", min_value=0, key="bj")
        ba = ba2.number_input("Adultos", min_value=0, key="ba")
        bs = ba3.number_input("Servos ", min_value=0, key="bs")

    # --- PROCESSAMENTO ---
    tot_comp9, tot_serv9 = (t9+v9+s9), (di9+me9+lo9)
    tot_mi9, tot_mpa9 = (mic9+mis9+mip9), (mpac9+mpas9+mpap9)
    tot_9h = tot_comp9 + tot_serv9 + tot_mi9 + tot_mpa9 + eb9

    tot_comp11, tot_serv11 = (t11+v11+s11), (di11+me11+lo11)
    tot_mi11, tot_bat = (mic11+mis11+mip11), (bj+ba+bs)
    tot_11h = tot_comp11 + tot_serv11 + tot_mi11 + tot_bat
    
    d9_str = d9_input.strftime('%d/%m/%Y') if d9_input else ""
    relatorio = f"Relatório de Cultos - PIB Floripa\n\nTotal 9h: {tot_9h}\nTotal 11h: {tot_11h}\nTOTAL GERAL: {tot_9h + tot_11h}"

    # --- BOTÕES PADRONIZADOS EM LINHA (A-P-W) ---
    st.markdown("---")
    col_arq, col_pla, col_wha = st.columns(3)

    with col_arq:
        # A - Arquivo em Texto
        show_manual = st.button("📄 Arquivo em Texto")

    with col_pla:
        # P - Planilha
        df_log = pd.DataFrame([{"Data": d9_str, "9h": tot_9h, "11h": tot_11h, "Total": tot_9h+tot_11h}])
        buf = BytesIO()
        with pd.ExcelWriter(buf, engine='xlsxwriter') as wr: df_log.to_excel(wr, index=False)
        st.download_button("📊 Planilha", buf.getvalue(), f"pib_{d9_str}.xlsx")

    with col_wha:
        # W - WhatsApp
        wa_link = f"https://wa.me/?text={urllib.parse.quote(relatorio)}"
        st.markdown(f'<a href="{wa_link}" target="_blank" class="btn-pib-custom">📲 WhatsApp</a>', unsafe_allow_html=True)

    if show_manual:
        st.info("Relatório gerado! Use o campo abaixo para copiar:")
        st.code(relatorio, language="text")

else:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.info("Por favor, insira a senha na barra lateral para acessar o sistema.")
