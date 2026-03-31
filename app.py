import streamlit as st
from datetime import date
import pandas as pd
from io import BytesIO
import urllib.parse

# Configuração visual
st.set_page_config(page_title="Relatório PIB474", page_icon="🌿", layout="centered")

# Cores em tons de verde - CORREÇÃO: unsafe_allow_html
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    .stButton>button { background-color: #2e7d32; color: white; width: 100%; border-radius: 8px; }
    .stExpander { border: 2px solid #a5d6a7; border-radius: 10px; background-color: #f1f8e9; }
    h1, h2, h3 { color: #1b5e20; }
    label { color: #2e7d32 !important; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

SENHA_CORRETA = "PIB474" 

st.sidebar.title("🔐 Acesso")
senha = st.sidebar.text_input("Senha:", type="password")

if senha == SENHA_CORRETA:
    st.title("🌿 Relatório de Cultos PIB474")
    
    # --- CULTO 09:00 ---
    with st.expander("🟢 CULTO DAS 09:00h - Clique para preencher", expanded=True):
        resp_9 = st.text_input("Responsável pela contagem (9h)", value="")
        data_9 = st.date_input("Data (9h)", value=None, format="DD/MM/YYYY")
        
        st.markdown("### 👥 Compareceram:")
        c1, c2, c3 = st.columns(3)
        temp_9 = c1.number_input("Templo e mezanino", min_value=0, key="t9")
        vis_9 = c2.number_input("Visitantes", min_value=0, key="v9")
        sex_9 = c3.number_input("Sexto andar", min_value=0, key="s9")
        
        st.markdown("### 🛠️ Servindo:")
        s1, s2, s3 = st.columns(3)
        dia_9 = s1.number_input("Diaconia", min_value=0, key="d9")
        mes_9 = s2.number_input("Mesa", min_value=0, key="m9")
        lou_9 = s3.number_input("Louvor", min_value=0, key="l9")

        st.markdown("### 👶 MI:")
        mi1, mi2, mi3 = st.columns(3)
        mi_c_9 = mi1.number_input("Crianças (MI 9h)", min_value=0)
        mi_s_9 = mi2.number_input("Servos (MI 9h)", min_value=0)
        mi_p_9 = mi3.number_input("Pai/Mãe (MI 9h)", min_value=0)

        st.markdown("### 🧒 MPA:")
        mp1, mp2, mp3 = st.columns(3)
        mpa_c_9 = mp1.number_input("Crianças (MPA 9h)", min_value=0)
        mpa_s_9 = mp2.number_input("Servos (MPA 9h)", min_value=0)
        mpa_p_9 = mp3.number_input("Pai/Mãe (MPA 9h)", min_value=0)
        
        ebed_9 = st.number_input("Ebed", min_value=0)

    # --- CULTO 11:00 ---
    with st.expander("🟢 CULTO DAS 11:00h - Clique para preencher", expanded=False):
        resp_11 = st.text_input("Responsável pela contagem (11h)", value="")
        data_11 = st.date_input("Data (11h)", value=None, format="DD/MM/YYYY")
        
        st.markdown("### 👥 Compareceram:")
        c4, c5, c6 = st.columns(3)
        temp_11 = c4.number_input("Templo e mezanino ", min_value=0, key="t11")
        vis_11 = c5.number_input("Visitantes ", min_value=0, key="v11")
        sex_11 = c6.number_input("Sexto andar ", min_value=0, key="s11")
        
        st.markdown("### 🛠️ Servindo:")
        s4, s5, s6 = st.columns(3)
        dia_11 = s4.number_input("Diaconia ", min_value=0, key="d11")
        mes_11 = s5.number_input("Mesa ", min_value=0, key="m11")
        lou_11 = s6.number_input("Louvor ", min_value=0, key="l11")

        st.markdown("### 👶 MI (11h):")
        mi4, mi5, mi6 = st.columns(3)
        mi_c_11 = mi4.number_input("Crianças (MI 11h)", min_value=0)
        mi_s_11 = mi5.number_input("Servos (MI 11h)", min_value=0)
        mi_p_11 = mi6.number_input("Pai/Mãe (MI 11h)", min_value=0)

        st.markdown("### 🎓 Classe Batismo:")
        ba1, ba2, ba3 = st.columns(3)
        bat_j = ba1.number_input("Jovens", min_value=0)
        bat_a = ba2.number_input("Adultos", min_value=0)
        bat_s = ba3.number_input("Servos ", min_value=0)

    # --- CÁLCULOS ---
    t_comp_9 = temp_9 + vis_9 + sex_9
    t_serv_9 = dia_9 + mes_9 + lou_9
    t_mi_9 = mi_c_9 + mi_s_9 + mi_p_9
    t_mpa_9 = mpa_c_9 + mpa_s_9 + mpa_p_9
    total_9h = t_comp_9 + t_serv_9 + t_mi_9 + t_mpa_9 + ebed_9

    t_comp_11 = temp_11 + vis_11 + sex_11
    t_serv_11 = dia_11 + mes_11 + lou_11
    t_mi_11 = mi_c_11 + mi_s_11 + mi_p_11
    t_bat_11 = bat_j + bat_a + bat_s
    total_11h = t_comp_11 + t_serv_11 + t_mi_11 + t_bat_11
    total_geral = total_9h + total_11h

    st.markdown("---")
    
    # Gerar Relatório Texto
    dt9 = data_9.strftime('%d/%m/%Y') if data_9 else ""
    dt11 = data_11.strftime('%d/%m/%Y') if data_11 else ""
    
    rel_texto = f"""Relatório dos cultos

Culto das 9:00hrs

Responsável pela contagem: {resp_9}
Data: {dt9}
Compareceram: 👥
Templo e mezanino: {temp_9}
Visitantes: {vis_9}
Sexto andar: {sex_9}
Total: {t_comp_9}

Servindo:
Diaconia: {dia_9}
Mesa: {mes_9}
Louvor: {lou_9}
Total: {t_serv_9}

MI:
Crianças: {mi_c_9}
Servos: {mi_s_9}
Pai/Mãe: {mi_p_9}
Total: {t_mi_9}

MPA:
Crianças: {mpa_c_9}
Servos: {mpa_s_9}
Pai/Mãe: {mpa_p_9}
Total: {t_mpa_9}

Ebed: {ebed_9}

TOTAL DO CULTO DAS 9:00hrs: {total_9h}

--------------------------------------

Culto das 11:00hrs

Responsável pela contagem: {resp_11}
Data: {dt11}
Compareceram: 👥
Templo e mezanino: {temp_11}
Visitantes: {vis_11}
Sexto andar: {sex_11}
Total: {t_comp_11}

Servindo:
Diaconia: {dia_11}
Mesa: {mes_11}
Louvor: {lou_11}
Total: {t_serv_11}

MI
Crianças: {mi_c_11}
Servos: {mi_s_11}
Pai/Mãe: {mi_p_11}
Total: {t_mi_11}

Classe batismo:
Jovens: {bat_j}
Adultos: {bat_a}
Servos: {bat_s}
Total: {t_bat_11}

TOTAL DO CULTO DAS 11:00hrs: {total_11h}

TOTAL GERAL: {total_geral}"""

    # BOTÕES DE AÇÃO
    col_wa, col_pla = st.columns(2)
    
    with col_wa:
        txt_wa = urllib.parse.quote(rel_texto)
        st.markdown(f'<a href="https://wa.me/?text={txt_wa}" target="_blank"><button style="width:100%; height:45px; background-color:#25D366; color:white; border:none; border-radius:10px; cursor:pointer; font-weight:bold;">📲 Enviar via WhatsApp</button></a>', unsafe_allow_html=True)
    
    with col_pla:
        # Criando uma planilha mais detalhada para o Google Sheets
        dados_planilha = {
            "Item": ["Total 9h", "Total 11h", "GERAL", "Templo 9h", "Templo 11h", "Ebed", "MI Total 9h", "MI Total 11h"],
            "Valores": [total_9h, total_11h, total_geral, temp_9, temp_11, ebed_9, t_mi_9, t_mi_11]
        }
        df = pd.DataFrame(dados_planilha)
        output = BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False)
        st.download_button("📥 Baixar Planilha (Excel)", data=output.getvalue(), file_name=f"pib474_{dt9}.xlsx")

    st.markdown("### 📋 Copiar Relatório Manualmente:")
    st.code(rel_texto, language="text")

else:
    st.info("Digite a senha PIB474 para liberar o relatório.")
