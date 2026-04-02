import streamlit as st
from datetime import date
import urllib.parse
import os

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Relatório PIB Floripa", page_icon="⛪", layout="centered")

# --- DESIGN E ESTILIZAÇÃO CSS ---
st.markdown("""
    <style>
    html, body, [class*="st-"] { font-size: 20px !important; }
    @media (max-width: 640px) {
        .stMarkdown, .stTextInput, .stNumberInput, label, p, .stDateInput { font-size: 22px !important; }
    }
    .stApp { background-color: #ffffff; }
    .pib-header-title { color: #004d40; font-size: 45px !important; font-weight: 800; text-align: center; margin-bottom: 0px; }
    .pib-header-subtitle { color: #004d40; font-size: 22px !important; text-align: center; margin-top: -10px; }
    .pib-faixa {
        background-color: #004d40; color: #ffffff !important; padding: 10px 15px;
        border-radius: 6px; font-size: 20px !important; font-weight: 600;
        margin-top: 25px; margin-bottom: 15px; display: flex; align-items: center; gap: 10px;
    }
    .faixa-center { justify-content: center; }
    .stExpander { border: 2px solid #a5d6a7; border-radius: 12px; background-color: #f1f8e9; margin-bottom: 20px; }
    label { color: #004d40 !important; font-weight: 700 !important; font-size: 20px !important; }
    .stTextInput>div>div>input, .stNumberInput>div>div>input, .stDateInput>div>div>input {
        height: 55px !important; font-size: 20px !important;
    }
    .fake-date-input {
        height: 55px; background-color: #f0f2f6; border: 1px solid rgba(49, 51, 63, 0.2);
        border-radius: 0.5rem; display: flex; align-items: center; padding: 0 1rem;
        color: #31333f; font-size: 20px; margin-bottom: 1rem;
    }
    .stButton>button, .btn-pib-custom {
        background-color: #004d40 !important; color: white !important;
        height: 65px !important; width: 100% !important; border-radius: 10px !important;
        font-weight: bold !important; font-size: 20px !important; display: flex !important;
        align-items: center !important; justify-content: center !important;
        text-decoration: none !important; margin-top: 10px;
    }
    .wa-confirm { background-color: #e8f5e9; padding: 20px; border-radius: 12px; border: 2px solid #2e7d32; text-align: center; font-size: 20px; }
    </style>
    """, unsafe_allow_html=True)

if 'autenticado' not in st.session_state: st.session_state.autenticado = False
if 'mostrar_relatorio' not in st.session_state: st.session_state.mostrar_relatorio = False
if 'wa_confirmar' not in st.session_state: st.session_state.wa_confirmar = False

# --- CABEÇALHO ---
col_logo, col_nome = st.columns([1, 3.5])
with col_logo:
    if os.path.exists("logo.png"): st.image("logo.png", width=110)
with col_nome:
    st.markdown('<p class="pib-header-title">PIB FLORIPA</p>', unsafe_allow_html=True)
    st.markdown('<p class="pib-header-subtitle">v1.2 - Sistema de Contagem</p>', unsafe_allow_html=True)

# --- ACESSO ---
if not st.session_state.autenticado:
    st.markdown("---")
    st.markdown("### 🔐 Autenticação")
    senha = st.text_input("Digite a senha para acessar o formulário:", type="password")
    if st.button("Entrar"):
        if senha.upper() == "PIB474":
            st.session_state.autenticado = True
            st.rerun()
        else: st.error("Senha incorreta")
else:
    st.markdown("---")
    
    # --- CULTO 09:00 ---
    with st.expander("🟢 CULTO DAS 09:00h - Preencher Dados", expanded=False):
        r9 = st.text_input("Responsável pela contagem (9h)", placeholder="Nome...", key="res9")
        d9_input = st.date_input("Data", value=None, format="DD/MM/YYYY", key="data_contagem_main")
        
        st.markdown('<div class="pib-faixa faixa-center">Compareceram</div>', unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        t9 = c1.number_input("Templo/Mezanino", value=None, step=1, key="t9")
        v9 = c2.number_input("Visitantes", value=None, step=1, key="v9")
        s9 = c3.number_input("Sexto andar", value=None, step=1, key="s9")
        
        st.markdown('<div class="pib-faixa">🛠️ Servindo</div>', unsafe_allow_html=True)
        s1, s2, s3 = st.columns(3)
        di9 = s1.number_input("Diaconia", value=None, step=1, key="di9")
        me9 = s2.number_input("Mesa", value=None, step=1, key="me9")
        lo9 = s3.number_input("Louvor", value=None, step=1, key="lo9")
        
        st.markdown('<div class="pib-faixa">🎒 MI (Ministério Infantil)</div>', unsafe_allow_html=True)
        mi1, mi2, mi3 = st.columns(3)
        mic9 = mi1.number_input("Crianças", value=None, step=1, key="mic9")
        mis9 = mi2.number_input("Servos", value=None, step=1, key="mis9")
        mip9 = mi3.number_input("Pai/Mãe", value=None, step=1, key="mip9")
        
        st.markdown('<div class="pib-faixa">🎮 MPA (Pré-Adolescente)</div>', unsafe_allow_html=True)
        mp1, mp2, mp3 = st.columns(3)
        mpac9 = mp1.number_input("Crianças ", value=None, step=1, key="mpac9")
        mpas9 = mp2.number_input("Servos ", value=None, step=1, key="mpas9")
        mpap9 = mp3.number_input("Pai/Mãe ", value=None, step=1, key="mpap9")
        
        st.markdown('<div class="pib-faixa">📚 Ebed</div>', unsafe_allow_html=True)
        eb9 = st.number_input("Total Ebed", value=None, step=1, key="eb9", label_visibility="collapsed")

    # --- CULTO 11:00 ---
    with st.expander("🟢 CULTO DAS 11:00h - Preencher Dados", expanded=False):
        r11 = st.text_input("Responsável pela contagem (11h)", placeholder="Nome...", key="res11")
        d_formatada = d9_input.strftime('%d/%m/%Y') if d9_input else "DD/MM/YYYY"
        st.markdown('<label>Data</label>', unsafe_allow_html=True)
        st.markdown(f'<div class="fake-date-input">{d_formatada}</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="pib-faixa faixa-center">Compareceram</div>', unsafe_allow_html=True)
        c4, c5, c6 = st.columns(3)
        t11 = c4.number_input("Templo/Mezanino  ", value=None, step=1, key="t11")
        v11 = c5.number_input("Visitantes  ", value=None, step=1, key="v11")
        s11 = c6.number_input("Sexto andar  ", value=None, step=1, key="s11")
        
        st.markdown('<div class="pib-faixa">🛠️ Servindo</div>', unsafe_allow_html=True)
        s4, s5, s6 = st.columns(3)
        di11 = s4.number_input("Diaconia  ", value=None, step=1, key="di11")
        me11 = s5.number_input("Mesa  ", value=None, step=1, key="me11")
        lo11 = s6.number_input("Louvor  ", value=None, step=1, key="lo11")

        st.markdown('<div class="pib-faixa">🎒 MI (Ministério Infantil)</div>', unsafe_allow_html=True)
        mi4, mi5, mi6 = st.columns(3)
        mic11 = mi4.number_input("Crianças  ", value=None, step=1, key="mic11")
        mis11 = mi5.number_input("Servos  ", value=None, step=1, key="mis11")
        mip11 = mi6.number_input("Pai/Mãe  ", value=None, step=1, key="mip11")

        st.markdown('<div class="pib-faixa">🎓 Classe Batismo</div>', unsafe_allow_html=True)
        ba1, ba2, ba3 = st.columns(3)
        bj = ba1.number_input("Jovens", value=None, step=1, key="bj")
        ba = ba2.number_input("Adultos", value=None, step=1, key="ba")
        bs = ba3.number_input("Servos   ", value=None, step=1, key="bs")

    # --- CÁLCULOS ---
    def nz(value): return int(value) if value is not None else 0

    t_c9, t_s9, t_mi9, t_mpa9 = (nz(t9)+nz(v9)+nz(s9)), (nz(di9)+nz(me9)+nz(lo9)), (nz(mic9)+nz(mis9)+nz(mip9)), (nz(mpac9)+nz(mpas9)+nz(mpap9))
    total_9h = t_c9 + t_s9 + t_mi9 + t_mpa9 + nz(eb9)
    
    t_c11, t_s11, t_mi11, t_bat = (nz(t11)+nz(v11)+nz(s11)), (nz(di11)+nz(me11)+nz(lo11)), (nz(mic11)+nz(mis11)+nz(mip11)), (nz(bj)+nz(ba)+nz(bs))
    total_11h = t_c11 + t_s11 + t_mi11 + t_bat

    d_rel = d9_input.strftime('%d/%m/%Y') if d9_input else "dd/mm/aaaa"
    
    rel_final = f"""Relatório dos cultos

Culto das 9:00hrs
Responsável pela contagem: {r9}
Data: {d_rel}

Compareceram
Templo e mezanino: {nz(t9)}
Visitantes: {nz(v9)}
Sexto andar: {nz(s9)}
Total: {t_c9}

Servindo:
Diaconia: {nz(di9)}
Mesa: {nz(me9)}
Louvor: {nz(lo9)}
Total: {t_s9}

MI:
Crianças: {nz(mic9)}
Servos: {nz(mis9)}
Pai/Mãe: {nz(mip9)}
Total: {t_mi9}

MPA:
Crianças: {nz(mpac9)}
Servos: {nz(mpas9)}
Pai/Mãe: {nz(mpap9)}
Total: {t_mpa9}

Ebed: {nz(eb9)}

TOTAL DO CULTO DAS 9:00hrs: {total_9h}

Culto das 11:00hrs
Responsável pela contagem: {r11}
Data: {d_rel}

Compareceram
Templo e mezanino: {nz(t11)}
Visitantes: {nz(v11)}
Sexto andar: {nz(s11)}
Total: {t_c11}

Servindo:
Diaconia: {nz(di11)}
Mesa: {nz(me11)}
Louvor: {nz(lo11)}
Total: {t_s11}

MI:
Crianças: {nz(mic11)}
Servos: {nz(mis11)}
Pai/Mãe: {nz(mip11)}
Total: {t_mi11}

Classe batismo:
Jovens: {nz(bj)}
Adultos: {nz(ba)}
Servos: {nz(bs)}
Total: {t_bat}

TOTAL DO CULTO DAS 11:00hrs: {total_11h}

TOTAL GERAL: {total_9h + total_11h}"""

    st.markdown("---")
    c_v, c_w = st.columns(2)
    if c_v.button("📄 Visualizar Relatório"): st.session_state.mostrar_relatorio = not st.session_state.mostrar_relatorio
    if c_w.button("📲 Enviar WhatsApp"): st.session_state.wa_confirmar = not st.session_state.wa_confirmar

    if st.session_state.wa_confirmar:
        st.markdown('<div class="wa-confirm"><strong>Confirmar envio do relatório para o WhatsApp?</strong></div>', unsafe_allow_html=True)
        wa_msg = f"```\n{rel_final}\n```"
        st.markdown(f'<a href="https://wa.me/?text={urllib.parse.quote(wa_msg)}" target="_blank" class="btn-pib-custom">Sim, Enviar Relatório</a>', unsafe_allow_html=True)

    if st.session_state.mostrar_relatorio: st.code(rel_final, language="text")

    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("🚪 Sair do Sistema"):
        st.session_state.autenticado = False
        st.rerun()
