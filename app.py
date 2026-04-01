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
        align-items: center; gap: 10px;
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
    .btn-sair > div > button { background-color: #c62828 !important; color: white !important; }
    
    /* Área de confirmação do WhatsApp */
    .wa-confirm {
        background-color: #e8f5e9;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #2e7d32;
        margin-top: 10px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SISTEMA DE ACESSO ---
if 'autenticado' not in st.session_state: st.session_state.autenticado = False
if 'mostrar_relatorio' not in st.session_state: st.session_state.mostrar_relatorio = False
if 'wa_confirmar' not in st.session_state: st.session_state.wa_confirmar = False

with st.sidebar:
    if not st.session_state.autenticado:
        senha = st.text_input("🔐 Autenticação:", type="password")
        if st.button("Entrar"):
            if senha.upper() == "PIB474":
                st.session_state.autenticado = True
                st.rerun()
            else: st.error("Senha incorreta")
    else:
        if st.button("🚪 Sair do Sistema", key="sair_btn"):
            st.session_state.autenticado = False
            st.rerun()

if st.session_state.autenticado:
    # --- CABEÇALHO ---
    col_logo, col_nome = st.columns([1, 3.5])
    with col_logo:
        if os.path.exists("logo.png"): st.image("logo.png", width=110)
    with col_nome:
        st.markdown('<p class="pib-header-title">PIB FLORIPA</p>', unsafe_allow_html=True)
        st.markdown('<p class="pib-header-subtitle">Primeira Igreja Batista de Florianópolis</p>', unsafe_allow_html=True)
        st.markdown('<p class="pib-rel-title">Relatório de Cultos</p>', unsafe_allow_html=True)
    
    # --- CULTO 09:00 ---
    with st.expander("🟢 CULTO DAS 09:00h - Preencher Dados", expanded=True):
        r9 = st.text_input("Responsável pela contagem (9h)", placeholder="Nome...", key="res9")
        d9_input = st.date_input("Data (9h)", value=None, format="DD/MM/YYYY", key="dat9")
        st.markdown('<div class="pib-faixa">👥 Compareceram</div>', unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        t9, v9, s9 = c1.number_input("Templo/Mezanino", 0, key="t9"), c2.number_input("Visitantes", 0, key="v9"), c3.number_input("Sexto andar", 0, key="s9")
        st.markdown('<div class="pib-faixa">🛠️ Servindo</div>', unsafe_allow_html=True)
        s1, s2, s3 = st.columns(3)
        di9, me9, lo9 = s1.number_input("Diaconia", 0, key="di9"), s2.number_input("Mesa", 0, key="me9"), s3.number_input("Louvor", 0, key="lo9")
        st.markdown('<div class="pib-faixa">🎒 MI (Ministério Infantil)</div>', unsafe_allow_html=True)
        mi1, mi2, mi3 = st.columns(3)
        mic9, mis9, mip9 = mi1.number_input("Crianças (MI)", 0, key="mic9"), mi2.number_input("Servos (MI)", 0, key="mis9"), mi3.number_input("Pai/Mãe (MI)", 0, key="mip9")
        st.markdown('<div class="pib-faixa">🎮 MPA (Pré-Adolescente)</div>', unsafe_allow_html=True)
        mp1, mp2, mp3 = st.columns(3)
        mpac9, mpas9, mpap9 = mp1.number_input("Crianças (MPA)", 0, key="mpac9"), mp2.number_input("Servos (MPA)", 0, key="mpas9"), mp3.number_input("Pai/Mãe (MPA)", 0, key="mpap9")
        eb9 = st.number_input("📚 Ebed", 0, key="eb9")

    # --- CULTO 11:00 ---
    with st.expander("🟢 CULTO DAS 11:00h - Preencher Dados", expanded=False):
        r11 = st.text_input("Responsável pela contagem (11h)", placeholder="Nome...", key="res11")
        d11_input = st.date_input("Data (11h)", value=None, format="DD/MM/YYYY", key="dat11")
        st.markdown('<div class="pib-faixa">👥 Compareceram</div>', unsafe_allow_html=True)
        c4, c5, c6 = st.columns(3)
        t11, v11, s11 = c4.number_input("Templo/Mezanino ", 0, key="t11"), c5.number_input("Visitantes ", 0, key="v11"), c6.number_input("Sexto andar ", 0, key="s11")
        st.markdown('<div class="pib-faixa">🛠️ Servindo</div>', unsafe_allow_html=True)
        s4, s5, s6 = st.columns(3)
        di11, me11, lo11 = s4.number_input("Diaconia ", 0, key="di11"), s5.number_input("Mesa ", 0, key="me11"), s6.number_input("Louvor ", 0, key="lo11")
        st.markdown('<div class="pib-faixa">🎒 MI (Ministério Infantil 11h)</div>', unsafe_allow_html=True)
        mi4, mi5, mi6 = st.columns(3)
        mic11, mis11, mip11 = mi4.number_input("Crianças (MI 11h)", 0, key="mic11"), mi5.number_input("Servos (MI 11h)", 0, key="mis11"), mi6.number_input("Pai/Mãe (MI 11h)", 0, key="mip11")
        st.markdown('<div class="pib-faixa">🎓 Classe Batismo</div>', unsafe_allow_html=True)
        ba1, ba2, ba3 = st.columns(3)
        bj, ba, bs = ba1.number_input("Jovens", 0, key="bj"), ba2.number_input("Adultos", 0, key="ba"), ba3.number_input("Servos ", 0, key="bs")

    # --- CÁLCULOS ---
    d9_s = d9_input.strftime('%d/%m/%Y') if d9_input else "dd/mm/aaaa"
    d11_s = d11_input.strftime('%d/%m/%Y') if d11_input else "dd/mm/aaaa"
    
    t_c9, t_s9, t_mi9, t_mpa9 = (t9+v9+s9), (di9+me9+lo9), (mic9+mis9+mip9), (mpac9+mpas9+mpap9)
    total_9h = t_c9 + t_s9 + t_mi9 + t_mpa9 + eb9
    
    t_c11, t_s11, t_mi11, t_bat = (t11+v11+s11), (di11+me11+lo11), (mic11+mis11+mip11), (bj+ba+bs)
    total_11h = t_c11 + t_s11 + t_mi11 + t_bat

    rel_modelo = f"""Relatório dos cultos

Culto das 9:00hrs
Responsável pela contagem: {r9}
Data: {d9_s}

Compareceram
Templo e mezanino: {t9}
Visitantes: {v9}
Sexto andar: {s9}
Total: {t_c9}

Servindo:
Diaconia: {di9}
Mesa: {me9}
Louvor: {lo9}
Total: {t_s9}

MI:
Crianças: {mic9}
Servos: {mis9}
Pai/Mãe: {mip9}
Total: {t_mi9}

MPA:
Crianças: {mpac9}
Servos: {mpas9}
Pai/Mãe: {mpap9}
Total: {t_mpa9}

Ebed: {eb9}
TOTAL DO CULTO DAS 9:00hrs: {total_9h}

Culto das 11:00hrs
Responsável pela contagem: {r11}
Data: {d11_s}

Compareceram
Templo e mezanino: {t11}
Visitantes: {v11}
Sexto andar: {s11}
Total: {t_c11}

Servindo:
Diaconia: {di11}
Mesa: {me11}
Louvor: {lo11}
Total: {t_s11}

MI:
Crianças: {mic11}
Servos: {mis11}
Pai/Mãe: {mip11}
Total: {t_mi11}

Classe batismo:
Jovens: {bj}
Adultos: {ba}
Servos: {bs}
Total: {t_bat}

TOTAL DO CULTO DAS 11:00hrs: {total_11h}

TOTAL GERAL: {total_9h + total_11h}"""

    # --- BOTÕES DE AÇÃO ---
    st.markdown("---")
    col_vis, col_wa = st.columns(2)
    
    with col_vis:
        if st.button("📄 Visualizar Relatório"):
            st.session_state.mostrar_relatorio = not st.session_state.mostrar_relatorio
            st.session_state.wa_confirmar = False

    with col_wa:
        if st.button("📲 WhatsApp"):
            st.session_state.wa_confirmar = not st.session_state.wa_confirmar
            st.session_state.mostrar_relatorio = False

    # --- LÓGICA DE EXIBIÇÃO ---
    if st.session_state.wa_confirmar:
        st.markdown('<div class="wa-confirm"><strong>Deseja enviar o relatório em qual formato?</strong></div>', unsafe_allow_html=True)
        cw1, cw2 = st.columns(2)
        with cw1:
            wa_t_link = f"https://wa.me/?text={urllib.parse.quote(rel_modelo)}"
            st.markdown(f'<a href="{wa_t_link}" target="_blank" class="btn-pib-custom">Texto</a>', unsafe_allow_html=True)
        with cw2:
            # Planilha via WhatsApp (Simulado via link do Excel gerado)
            df_wa = pd.DataFrame([{"Data": d9_s, "Total 9h": total_9h, "Total 11h": total_11h, "Geral": total_9h+total_11h}])
            buf = BytesIO()
            with pd.ExcelWriter(buf) as wr: df_wa.to_excel(wr, index=False)
            st.download_button("Planilha (Download)", buf.getvalue(), f"pib_{d9_s}.xlsx", use_container_width=True)

    if st.session_state.mostrar_relatorio:
        st.markdown("### Relatório Gerado")
        st.code(rel_modelo, language="text")
