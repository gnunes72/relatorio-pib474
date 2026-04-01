import streamlit as st
from datetime import date
import urllib.parse
import os

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Relatório PIB Floripa", page_icon="⛪", layout="centered")

# --- DESIGN E ESTILIZAÇÃO CSS (Foco em Mobile e Fontes Grandes) ---
st.markdown("""
    <style>
    /* Estilos Globais e Mobile First */
    html, body, [class*="st-"] {
        font-size: 20px !important;
    }
    
    /* Forçar fonte maior em telas pequenas (Celulares) */
    @media (max-width: 640px) {
        .stMarkdown, .stTextInput, .stNumberInput, label, p {
            font-size: 22px !important;
        }
        .st-emotion-cache-p5m613 { font-size: 24px !important; } /* Título Expander */
    }

    .stApp { background-color: #ffffff; }
    .pib-header-title { color: #004d40; font-size: 45px !important; font-weight: 800; text-align: center; margin-bottom: 0px; }
    .pib-header-subtitle { color: #004d40; font-size: 22px !important; text-align: center; margin-top: -10px; }
    
    .pib-faixa {
        background-color: #004d40;
        color: #ffffff !important;
        padding: 10px 15px;
        border-radius: 6px;
        font-size: 20px !important;
        font-weight: 600;
        margin-top: 25px;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .faixa-center { justify-content: center; }

    .stExpander { border: 2px solid #a5d6a7; border-radius: 12px; background-color: #f1f8e9; margin-bottom: 20px; }
    
    label { 
        color: #004d40 !important; 
        font-weight: 700 !important; 
        font-size: 20px !important; 
    }

    /* Aumentar altura dos campos de input para mobile */
    .stTextInput>div>div>input, .stNumberInput>div>div>input {
        height: 50px !important;
        font-size: 20px !important;
    }

    .stButton>button, .btn-pib-custom {
        background-color: #004d40 !important;
        color: white !important;
        height: 65px !important;
        width: 100% !important;
        border-radius: 10px !important;
        font-weight: bold !important;
        font-size: 20px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        text-decoration: none !important;
        margin-top: 10px;
    }
    .wa-confirm { background-color: #e8f5e9; padding: 20px; border-radius: 12px; border: 2px solid #2e7d32; text-align: center; font-size: 20px; }
    
    /* Ajuste do título do Expander */
    .st-emotion-cache-p5m613 { font-size: 22px !important; font-weight: bold !important; color: #004d40 !important; }
    
    /* Info box para data espelhada */
    .data-espelhada {
        background-color: #e8f5e9;
        padding: 10px;
        border-radius: 8px;
        border-left: 5px solid #2e7d32;
        font-weight: bold;
        color: #004d40;
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

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
        if st.button("🚪 Sair"):
            st.session_state.autenticado = False
            st.rerun()

if st.session_state.autenticado:
    col_logo, col_nome = st.columns([1, 3.5])
    with col_logo:
        if os.path.exists("logo.png"): st.image("logo.png", width=110)
    with col_nome:
        st.markdown('<p class="pib-header-title">PIB FLORIPA</p>', unsafe_allow_html=True)
        st.markdown('<p class="pib-header-subtitle">Primeira Igreja Batista de Florianópolis</p>', unsafe_allow_html=True)
    
    # --- CULTO 09:00 ---
    with st.expander("🟢 CULTO DAS 09:00h - Preencher Dados", expanded=False):
        r9 = st.text_input("Responsável pela contagem (9h)", placeholder="Nome...", key="res9")
        d9_input = st.date_input("Data", value=None, format="DD/MM/YYYY", key="dat9")
        
        st.markdown('<div class="pib-faixa faixa-center">Compareceram</div>', unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        t9, v9, s9 = c1.number_input("Templo/Mezanino", 0, key="t9"), c2.number_input("Visitantes", 0, key="v9"), c3.number_input("Sexto andar", 0, key="s9")
        
        st.markdown('<div class="pib-faixa">🛠️ Servindo</div>', unsafe_allow_html=True)
        s1, s2, s3 = st.columns(3)
        di9, me9, lo9 = s1.number_input("Diaconia", 0, key="di9"), s2.number_input("Mesa", 0, key="me9"), s3.number_input("Louvor", 0, key="lo9")
        
        st.markdown('<div class="pib-faixa">🎒 MI (Ministério Infantil)</div>', unsafe_allow_html=True)
        mi1, mi2, mi3 = st.columns(3)
        mic9, mis9, mip9 = mi1.number_input("Crianças", 0, key="mic9"), mi2.number_input("Servos", 0, key="mis9"), mi3.number_input("Pai/Mãe", 0, key="mip9")
        
        st.markdown('<div class="pib-faixa">🎮 MPA (Pré-Adolescente)</div>', unsafe_allow_html=True)
        mp1, mp2, mp3 = st.columns(3)
        mpac9, mpas9, mpap9 = mp1.number_input("Crianças", 0, key="mpac9"), mp2.number_input("Servos", 0, key="mpas9"), mp3.number_input("Pai/Mãe", 0, key="mpap9")
        
        st.markdown('<div class="pib-faixa">📚 Ebed</div>', unsafe_allow_html=True)
        eb9 = st.number_input("Total Ebed", 0, key="eb9", label_visibility="collapsed")

    # --- CULTO 11:00 ---
    with st.expander("🟢 CULTO DAS 11:00h - Preencher Dados", expanded=False):
        r11 = st.text_input("Responsável pela contagem (11h)", placeholder="Nome...", key="res11")
        
        # Ajuste Data: Exibição dinâmica
        d_formatada = d9_input.strftime('%d/%m/%Y') if d9_input else "Aguardando data das 09h..."
        st.markdown(f'<div class="data-espelhada">📅 Data: {d_formatada}</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="pib-faixa faixa-center">Compareceram</div>', unsafe_allow_html=True)
        c4, c5, c6 = st.columns(3)
        t11, v11, s11 = c4.number_input("Templo/Mezanino ", 0, key="t11"), c5.number_input("Visitantes ", 0, key="v11"), c6.number_input("Sexto andar ", 0, key="s11")
        
        st.markdown('<div class="pib-faixa">🛠️ Servindo</div>', unsafe_allow_html=True)
        s4, s5, s6 = st.columns(3)
        di11, me11, lo11 = s4.number_input("Diaconia ", 0, key="di11"), s5.number_input("Mesa ", 0, key="me11"), s6.number_input("Louvor ", 0, key="lo11")

        st.markdown('<div class="pib-faixa">🎒 MI (Ministério Infantil)</div>', unsafe_allow_html=True)
        mi4, mi5, mi6 = st.columns(3)
        mic11, mis11, mip11 = mi4.number_input("Crianças ", 0, key="mic11"), mi5.number_input("Servos ", 0, key="mis11"), mi6.number_input("Pai/Mãe ", 0, key="mip11")

        st.markdown('<div class="pib-faixa">🎓 Classe Batismo</div>', unsafe_allow_html=True)
        ba1, ba2, ba3 = st.columns(3)
        bj, ba, bs = ba1.number_input("Jovens", 0, key="bj"), ba2.number_input("Adultos", 0, key="ba"), ba3.number_input("Servos ", 0, key="bs")

    # --- CÁLCULOS E RELATÓRIO ---
    d_s = d9_input.strftime('%d/%m/%Y') if d9_input else "dd/mm/aaaa"
    t_c9, t_s9, t_mi9, t_mpa9 = (t9+v9+s9), (di9+me9+lo9), (mic9+mis9+mip9), (mpac9+mpas9+mpap9)
    total_9h = t_c9 + t_s9 + t_mi9 + t_mpa9 + eb9
    t_c11, t_s11, t_mi11, t_bat = (t11+v11+s11), (di11+me11+lo11), (mic11+mis11+mip11), (bj+ba+bs)
    total_11h = t_c11 + t_s11 + t_mi11 + t_bat

    rel_final = f"""Relatório dos cultos

Culto das 9:00hrs
Responsável pela contagem: {r9}
Data: {d_s}

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
Data: {d_s}

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

    st.markdown("---")
    c_v, c_w = st.columns(2)
    with c_v:
        if st.button("📄 Visualizar Relatório"): st.session_state.mostrar_relatorio = not st.session_state.mostrar_relatorio
    with c_w:
        if st.button("📲 Enviar WhatsApp"): st.session_state.wa_confirmar = not st.session_state.wa_confirmar

    if st.session_state.wa_confirmar:
        st.markdown('<div class="wa-confirm"><strong>Confirmar envio do relatório para o WhatsApp?</strong></div>', unsafe_allow_html=True)
        wa_msg = f"```\n{rel_final}\n```"
        st.markdown(f'<a href="https://wa.me/?text={urllib.parse.quote(wa_msg)}" target="_blank" class="btn-pib-custom">Sim, Enviar Relatório</a>', unsafe_allow_html=True)

    if st.session_state.mostrar_relatorio:
        st.code(rel_final, language="text")
