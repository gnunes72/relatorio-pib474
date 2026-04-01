import streamlit as st
from datetime import date
import pandas as pd
from io import BytesIO
import urllib.parse
from PIL import Image
import os

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Relatório PIB Floripa", page_icon="⛪", layout="centered")

# --- DESIGN E ESTILIZAÇÃO CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    .pib-header-title { color: #004d40; font-size: 42px !important; font-weight: 800; margin-bottom: 0px; text-align: center; }
    .pib-header-subtitle { color: #004d40; font-size: 19px !important; margin-top: -10px; margin-bottom: 5px; text-align: center; }
    .pib-rel-title { color: #2e7d32; font-size: 15px !important; text-align: center; font-weight: bold; text-transform: uppercase; margin-bottom: 25px; }
    
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
    }

    .stExpander { border: 1px solid #a5d6a7; border-radius: 10px; background-color: #f1f8e9; margin-bottom: 15px; }
    label { color: #004d40 !important; font-weight: 700 !important; }

    /* BOTÕES PADRONIZADOS */
    .stButton>button, .btn-pib-custom {
        background-color: #004d40 !important;
        color: white !important;
        height: 50px !important;
        width: 100% !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        font-size: 14px !important;
        border: none !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        gap: 10px !important;
        text-decoration: none !important;
    }
    /* Botão Sair Vermelho */
    .btn-sair > div > button {
        background-color: #c62828 !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SISTEMA DE ACESSO ---
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False

with st.sidebar:
    if not st.session_state.autenticado:
        senha = st.text_input("🔐 Autenticação:", type="password")
        if st.button("Entrar"):
            if senha.upper() == "PIB474":
                st.session_state.autenticado = True
                st.rerun()
            else:
                st.error("Senha incorreta")
    else:
        st.markdown(f"**Usuário:** PIB474")
        st.markdown('<div class="btn-sair">', unsafe_allow_html=True)
        if st.button("🚪 Sair do Sistema"):
            st.session_state.autenticado = False
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.autenticado:
    
    # --- CABEÇALHO ---
    col_logo, col_nome = st.columns([1, 3.5])
    with col_logo:
        if os.path.exists("logo.png"): st.image("logo.png", width=110)
    with col_nome:
        st.markdown('<p class="pib-header-title">PIB FLORIPA</p>', unsafe_allow_html=True)
        st.markdown('<p class="pib-header-subtitle">Primeira Igreja Batista de Florianópolis</p>', unsafe_allow_html=True)
        st.markdown('<p class="pib-rel-title">Relatório Detalhado de Cultos</p>', unsafe_allow_html=True)
    
    # --- CULTO 09:00 ---
    with st.expander("🟢 CULTO DAS 09:00h - Preencher Dados", expanded=True):
        r9 = st.text_input("Responsável (9h)", placeholder="Nome...", key="res9")
        d9_input = st.date_input("Data (9h)", value=None, format="DD/MM/YYYY", key="dat9")
        
        st.markdown('<div class="pib-faixa">👥 Compareceram</div>', unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        t9, v9, s9 = c1.number_input("Templo", 0, key="t9"), c2.number_input("Visitantes", 0, key="v9"), c3.number_input("6º Andar", 0, key="s9")
        
        st.markdown('<div class="pib-faixa">🛠️ Servindo</div>', unsafe_allow_html=True)
        s1, s2, s3 = st.columns(3)
        di9, me9, lo9 = s1.number_input("Diaconia", 0, key="di9"), s2.number_input("Mesa", 0, key="me9"), s3.number_input("Louvor", 0, key="lo9")

        st.markdown('<div class="pib-faixa">🎒 MI (Infantil)</div>', unsafe_allow_html=True)
        mi1, mi2, mi3 = st.columns(3)
        mic9, mis9, mip9 = mi1.number_input("Crianças (MI)", 0, key="mic9"), mi2.number_input("Servos (MI)", 0, key="mis9"), mi3.number_input("Pais (MI)", 0, key="mip9")

        st.markdown('<div class="pib-faixa">🎮 MPA (Adolescentes)</div>', unsafe_allow_html=True)
        mp1, mp2, mp3 = st.columns(3)
        mpac9, mpas9, mpap9 = mp1.number_input("Crianças (MPA)", 0, key="mpac9"), mp2.number_input("Servos (MPA)", 0, key="mpas9"), mp3.number_input("Pais (MPA)", 0, key="mpap9")
        
        eb9 = st.number_input("📚 Total Ebed", 0, key="eb9")

    # --- CULTO 11:00 ---
    with st.expander("🟢 CULTO DAS 11:00h - Preencher Dados", expanded=False):
        r11 = st.text_input("Responsável (11h)", placeholder="Nome...", key="res11")
        st.markdown('<div class="pib-faixa">👥 Compareceram</div>', unsafe_allow_html=True)
        c4, c5, c6 = st.columns(3)
        t11, v11, s11 = c4.number_input("Templo ", 0, key="t11"), c5.number_input("Visitantes ", 0, key="v11"), c6.number_input("6º Andar ", 0, key="s11")
        
        st.markdown('<div class="pib-faixa">🛠️ Servindo</div>', unsafe_allow_html=True)
        s4, s5, s6 = st.columns(3)
        di11, me11, lo11 = s4.number_input("Diaconia ", 0, key="di11"), s5.number_input("Mesa ", 0, key="me11"), s6.number_input("Louvor ", 0, key="lo11")

        st.markdown('<div class="pib-faixa">🎒 MI (Infantil 11h)</div>', unsafe_allow_html=True)
        mi4, mi5, mi6 = st.columns(3)
        mic11, mis11, mip11 = mi4.number_input("Crianças (MI 11h)", 0, key="mic11"), mi5.number_input("Servos (MI 11h)", 0, key="mis11"), mi6.number_input("Pais (MI 11h)", 0, key="mip11")

        st.markdown('<div class="pib-faixa">🎓 Classe Batismo</div>', unsafe_allow_html=True)
        ba1, ba2, ba3 = st.columns(3)
        bj, ba, bs = ba1.number_input("Jovens", 0, key="bj"), ba2.number_input("Adultos", 0, key="ba"), ba3.number_input("Servos ", 0, key="bs")

    # --- PROCESSAMENTO DETALHADO ---
    tot_9h = (t9+v9+s9) + (di9+me9+lo9) + (mic9+mis9+mip9) + (mpac9+mpas9+mpap9) + eb9
    tot_11h = (t11+v11+s11) + (di11+me11+lo11) + (mic11+mis11+mip11) + (bj+ba+bs)
    d_str = d9_input.strftime('%d/%m/%Y') if d9_input else ""

    relatorio_detalhado = f"""⛪ PIB FLORIPA - RELATÓRIO {d_str}

🟢 CULTO 09:00h
Responsável: {r9}
- Compareceram: {t9+v9+s9} (T: {t9}, V: {v9}, 6º: {s9})
- Servindo: {di9+me9+lo9} (Diac: {di9}, Mesa: {me9}, Louv: {lo9})
- MI: {mic9+mis9+mip9} | MPA: {mpac9+mpas9+mpap9}
- Ebed: {eb9}
TOTAL 9h: {tot_9h}

🟢 CULTO 11:00h
Responsável: {r11}
- Compareceram: {t11+v11+s11} (T: {t11}, V: {v11}, 6º: {s11})
- Servindo: {di11+me11+lo11} (Diac: {di11}, Mesa: {me11}, Louv: {lo11})
- MI 11h: {mic11+mis11+mip11}
- Batismo: {bj+ba+bs}
TOTAL 11h: {tot_11h}

📊 TOTAL GERAL DO DIA: {tot_9h + tot_11h} pessoas"""

    # --- BOTÕES A-P-W ---
    st.markdown("---")
    col_arq, col_pla, col_wha = st.columns(3)

    with col_arq:
        show_rel = st.button("📄 Arquivo em Texto")
    with col_pla:
        df = pd.DataFrame([{"Data": d_str, "Total 9h": tot_9h, "Total 11h": tot_11h, "Geral": tot_9h+tot_11h}])
        buf = BytesIO()
        with pd.ExcelWriter(buf) as wr: df.to_excel(wr, index=False)
        st.download_button("📊 Planilha", buf.getvalue(), f"pib_{d_str}.xlsx")
    with col_wha:
        wa_link = f"https://wa.me/?text={urllib.parse.quote(relatorio_detalhado)}"
        st.markdown(f'<a href="{wa_link}" target="_blank" class="btn-pib-custom">📲 WhatsApp</a>', unsafe_allow_html=True)

    if show_rel:
        st.code(relatorio_detalhado, language="text")
else:
    st.info("Insira a senha na barra lateral.")
