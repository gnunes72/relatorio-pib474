import streamlit as st
from datetime import date

# Configuração da página
st.set_page_config(page_title="Relatório PIB474", page_icon="⛪")

# --- SENHA DE ACESSO ---
SENHA_CORRETA = "PIB474" 

st.sidebar.title("🔐 Acesso")
senha = st.sidebar.text_input("Digite a senha:", type="password")

if senha == SENHA_CORRETA:
    st.title("⛪ Relatório dos Cultos")
    
    # --- CULTO 09:00 ---
    with st.expander("📝 Dados do Culto das 09:00h", expanded=True):
        resp_9 = st.text_input("Responsável (9h)", value="Giovane")
        data_hj = st.date_input("Data", date.today())
        
        c1, c2, c3 = st.columns(3)
        temp_9 = c1.number_input("Templo/Mezanino", min_value=0, key="t9")
        vis_9 = c2.number_input("Visitantes", min_value=0, key="v9")
        sex_9 = c3.number_input("6º Andar", min_value=0, key="s9")
        
        st.write("**Servindo (9h):**")
        s1, s2, s3 = st.columns(3)
        dia_9 = s1.number_input("Diaconia", min_value=0, key="d9")
        mes_9 = s2.number_input("Mesa", min_value=0, key="m9")
        lou_9 = s3.number_input("Louvor", min_value=0, key="l9")

        st.write("**Kids (MI e MPA 9h):**")
        k1, k2, k3 = st.columns(3)
        mi_9 = k1.number_input("Total MI", min_value=0, help="Crianças+Servos+Pais", key="mi9")
        mpa_9 = k2.number_input("Total MPA", min_value=0, help="Crianças+Servos+Pais", key="mpa9")

    # --- CULTO 11:00 ---
    with st.expander("📝 Dados do Culto das 11:00h"):
        resp_11 = st.text_input("Responsável (11h)", value="Giovane")
        
        c4, c5, c6 = st.columns(3)
        temp_11 = c4.number_input("Templo/Mezanino", min_value=0, key="t11")
        vis_11 = c5.number_input("Visitantes", min_value=0, key="v11")
        sex_11 = c6.number_input("6º Andar", min_value=0, key="s11")
        
        st.write("**Servindo (11h):**")
        s4, s5, s6 = st.columns(3)
        dia_11 = s4.number_input("Diaconia", min_value=0, key="d11")
        mes_11 = s5.number_input("Mesa", min_value=0, key="m11")
        lou_11 = s6.number_input("Louvor", min_value=0, key="l11")

        st.write("**Kids (MI 11h):**")
        mi_11 = st.number_input("Total MI (11h)", min_value=0, key="mi11")

    # --- CÁLCULOS ---
    t_9 = temp_9 + vis_9 + sex_9 + dia_9 + mes_9 + lou_9 + mi_9 + mpa_9
    t_11 = temp_11 + vis_11 + sex_11 + dia_11 + mes_11 + lou_11 + mi_11
    geral = t_9 + t_11

    if st.button("GERAR RELATÓRIO PARA WHATSAPP", use_container_width=True):
        texto = f"""Relatório dos cultos
Data: {data_hj.strftime('%d/%m/%Y')}

Culto das 9:00hrs
Responsável: {resp_9}
Templo/Mezanino: {temp_9} | Visitantes: {vis_9} | 6º Andar: {sex_9}
Total Público: {temp_9+vis_9+sex_9}

Servindo: Diaconia {dia_9}, Mesa {mes_9}, Louvor {lou_9}
MI: {mi_9} | MPA: {mpa_9}

TOTAL DAS 9:00h: {t_9}

---------------------------

Culto das 11:00hrs
Responsável: {resp_11}
Templo/Mezanino: {temp_11} | Visitantes: {vis_11} | 6º Andar: {sex_11}
Total Público: {temp_11+vis_11+sex_11}

Servindo: Diaconia {dia_11}, Mesa {mes_11}, Louvor {lou_11}
MI: {mi_11}

TOTAL DAS 11:00h: {t_11}

TOTAL GERAL: {geral}"""
        
        st.code(texto, language="text")
        st.success("Copie o texto acima!")

else:
    st.warning("Aguardando senha PIB474...")
