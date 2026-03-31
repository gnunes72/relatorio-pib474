import streamlit as st
from datetime import date
import pandas as pd
from io import BytesIO
import urllib.parse
from PIL import Image
import os

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Relatório PIB Floripa", page_icon="⛪", layout="centered")

# --- DESIGN E ESTILIZAÇÃO CSS (Padrão PIB Floripa) ---
# Cores PIB: Verde Escuro #005a3c | Verde Claro Fundo #e8f5e9
st.markdown("""
    <style>
    /* Estilo do Fundo e Títulos Principais */
    .stApp { background-color: #ffffff; }
    h1 { color: #005a3c; font-size: 34px !important; margin-bottom: 0px; text-align: center; }
    h2 { color: #005a3c; font-size: 20px !important; font-weight: normal; margin-top: 0px; margin-bottom: 30px; text-align: center; }
    
    /* Estilo dos Subtítulos (Compareceram, Servindo, etc.) com Faixa Verde */
    .pib-subtitulo {
        background-color: #005a3c;
        color: white !important;
        padding: 8px 15px;
        border-radius: 5px;
        font-size: 14px !important; /* Tamanho da fonte conforme solicitado */
        font-weight: bold;
        margin-top: 20px;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    /* Estilo dos Containers de Dados (Verde Claríssimo para preenchimento) */
    .stExpander { border: 1px solid #a5d6a7; border-radius: 8px; background-color: #e8f5e9; margin-bottom: 20px; }
    
    /* Estilo de Inputs */
    .stNumberInput label, .stTextInput label, .stDateInput label { color: #005a3c !important; font-weight: bold; font-size: 13px; }
    
    /* --- PADRONIZAÇÃO TOTAL DOS BOTÕES DE AÇÃO --- */
    .stButton>button, .btn-pib-wa {
        background-color: #005a3c !important; /* MESMA COR VERDE */
        color: white !important; /* TEXTO BRANCO */
        height: 48px !important; /* MESMA ALTURA */
        width: 100% !important; /* OCUPA TODA A COLUNA */
        border-radius: 5px !important;
        font-weight: bold !important;
        font-size: 14px !important; /* MESMO TAMANHO DE FONTE QUE OS SUBTÍTULOS */
        border: none !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        gap: 10px !important; /* ESPAÇO ÍCONE-TEXTO */
        text-decoration: none !important;
        transition: 0.3s;
    }
    .stButton>button:hover, .btn-pib-wa:hover { background-color: #004d30 !important; }
    
    /* Ajuste de ícones */
    .css-1offfwp, .stButton>button div, .btn-pib-wa div { font-family: "Apple Color Emoji", "Segoe UI Emoji", "Noto Color Emoji", sans-serif !important; }
    </style>
    """, unsafe_allow_html=True)

# --- SENHA DE ACESSO (Maiúsculas/Minúsculas) ---
SENHA_DEFINIDA = "PIB474" 

st.sidebar.markdown(f'<div class="pib-subtitulo">🔐 Acesso Restrito</div>', unsafe_allow_html=True)
senha_digitada = st.sidebar.text_input("Senha:", type="password")

# Verifica senha aceitando qualquer combinação de maiúsculas/minúsculas
if senha_digitada.upper() == SENHA_DEFINIDA:
    
    # --- CABEÇALHO (LOGO E NOMES) ---
    col_logo, col_nome = st.columns([1, 4])
    with col_logo:
        # Tenta carregar o logo.png do repositório
        if os.path.exists("logo.png"):
            st.image("logo.png", width=90)
        else:
            st.warning("Suba o logo.png para o GitHub")
            
    with col_nome:
        st.markdown("<h1>PIB Floripa</h1>", unsafe_allow_html=True)
        st.markdown("<h2>Primeira Igreja Batista de Florianópolis - Relatório de Cultos</h2>", unsafe_allow_html=True)
    
    # --- CULTO 09:00 ---
    with st.expander("🟢 DADOS DO CULTO DAS 09:00h", expanded=True):
        resp_9 = st.text_input("Responsável pela contagem (9h)", value="", key="r9")
        data_9 = st.date_input("Data (9h)", value=None, format="DD/MM/YYYY", key="d9")
        
        # Subtítulo Compareceram
        st.markdown('<div class="pib-subtitulo">👥 Compareceram</div>', unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        temp_9 = c1.number_input("Templo e mezanino", min_value=0, key="t9_")
        vis_9 = c2.number_input("Visitantes", min_value=0, key="v9_")
        sex_9 = c3.number_input("Sexto andar", min_value=0, key="s9_")
        
        # Subtítulo Servindo
        st.markdown('<div class="pib-subtitulo">🛠️ Servindo</div>', unsafe_allow_html=True)
        s1, s2, s3 = st.columns(3)
        dia_9 = s1.number_input("Diaconia", min_value=0, key="d9_")
        mes_9 = s2.number_input("Mesa", min_value=0, key="m9_")
        lou_9 = s3.number_input("Louvor", min_value=0, key="l9_")

        # Subtítulo MI (Infantil)
        st.markdown('<div class="pib-subtitulo">🎒 MI (Ministério Infantil)</div>', unsafe_allow_html=True)
        mi1, mi2, mi3 = st.columns(3)
        mi_c_9 = mi1.number_input("Crianças (MI)", min_value=0, key="mic9_")
        mi_s_9 = mi2.number_input("Servos (MI)", min_value=0, key="mis9_")
        mi_p_9 = mi3.number_input("Pai/Mãe (MI)", min_value=0, key="mip9_")

        # Subtítulo MPA (Pré-Adolescente)
        st.markdown('<div class="pib-subtitulo">🎮 MPA (Pré-Adolescente)</div>', unsafe_allow_html=True)
        mp1, mp2, mp3 = st.columns(3)
        mpa_c_9 = mp1.number_input("Crianças (MPA)", min_value=0, key="mpac9_")
        mpa_s_9 = mp2.number_input("Servos (MPA)", min_value=0, key="mpas9_")
        mpa_p_9 = mp3.number_input("Pai/Mãe (MPA)", min_value=0, key="mpap9_")
        
        # Subtítulo Ebed
        st.markdown('<div class="pib-subtitulo">📚 Ebed</div>', unsafe_allow_html=True)
        ebed_9 = st.number_input("Total Ebed", min_value=0, key="e9_", label_visibility="collapsed")

    # --- CULTO 11:00 ---
    with st.expander("🟢 DADOS DO CULTO DAS 11:00h", expanded=False):
        resp_11 = st.text_input("Responsável pela contagem (11h)", value="", key="r11")
        data_11 = st.date_input("Data (11h)", value=None, format="DD/MM/YYYY", key="d11")
        
        st.markdown('<div class="pib-faixa">👥 Compareceram</div>', unsafe_allow_html=True)
        c4, c5, c6 = st.columns(3)
        t11 = c4.number_input("Templo ", min_value=0, key="t11_")
        v11 = c5.number_input("Visitantes ", min_value=0, key="v11_")
        s11 = c6.number_input("Sexto andar ", min_value=0, key="s11_")
        
        st.markdown('<div class="pib-faixa">🛠️ Servindo</div>', unsafe_allow_html=True)
        di11 = st.number_input("Diaconia ", min_value=0, key="di11_")

    # --- CÁLCULOS ---
    total_9h = (temp_9+vis_9+sex_9) + (dia_9+mes_9+lou_9) + (mi_c_9+mi_s_9+mi_p_9) + (mpa_c_9+mpa_s_9+mpa_p_9) + ebed_9
    total_11h = (t11+v11+s11) + (di11)
    
    total_geral = total_9h + total_11h

    # --- GERAÇÃO DO TEXTO DO RELATÓRIO ---
    dt9 = data_9.strftime('%d/%m/%Y') if data_9 else ""
    rel_texto = f"""Relatório de Cultos - PIB Floripa - Data: {dt9}\nTotal Geral: {total_geral}\nCulto 9h: {total_9h}\nCulto 11h: {total_11h}"""

    # --- BOTÕES DE AÇÃO (ORDEM E PADRONIZAÇÃO EXATAS) ---
    st.markdown("---")
    col_t, col_p, col_w = st.columns(3) # Ordem Alfabética: Arquivo, Planilha, WhatsApp

    # 1. ARQUIVO EM TEXTO (Ordem: A)
    with col_t:
        st.write("") # Pequeno ajuste de alinhamento
        # Ícone LATERAL e Texto PADRONIZADO
        btn_texto_label = "📄 Arquivo em Texto"
        show_text = st.button(btn_texto_label)

    # 2. PLANILHA (Ordem: P)
    with col_p:
        st.write("")
        df = pd.DataFrame([{"Data": dt9, "9h": total_9h, "11h": total_11h, "Geral": total_geral}])
        output = BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer: df.to_excel(writer, index=False)
        # Botão PADRONIZADO (Verde, Tamanho, Fonte) com Ícone LATERAL
        btn_planilha_label = "📊 Planilha"
        st.download_button(btn_planilha_label, data=output.getvalue(), file_name=f"pib_floripa_{dt9}.xlsx")

    # 3. WHATSAPP (Ordem: W)
    with col_w:
        st.write("")
        texto_wa = urllib.parse.quote(rel_texto)
        link_wa = f"https://wa.me/?text={texto_wa}"
        # Botão PADRONIZADO (Verde, Tamanho, Fonte) com Ícone LATERAL
        # Usamos markdown para o link, mas replicamos a classe CSS do botão Streamlit
        st.markdown(f'<a href="{link_wa}" target="_blank" class="btn-pib-wa"><div>📲 WhatsApp</div></a>', unsafe_allow_html=True)

    # --- CÓPIA MANUAL ESCONDIDA ---
    st.markdown("---")
    with st.expander("📋 CÓPIA MANUAL (Clique para abrir e copiar)", expanded=False):
        st.markdown("### Copie o relatório abaixo:")
        st.code(rel_texto, language="text")

else:
    # Tela de senha (simples)
    st.markdown("<h1 style='text-align: center; color: #005a3c;'>PIB Floripa</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: #005a3c;'>Aguardando senha PIB474...</h2>", unsafe_allow_html=True)
