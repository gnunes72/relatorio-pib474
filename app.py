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
    with st.expander("📝 DADOS DO CULTO DAS 09:00h", expanded=True):
        resp_9 = st.text_input("Responsável pela contagem (9h)", value="")
        data_9 = st.date_input("Data (9h)", value=None, format="DD/MM/YYYY")
        comp_9 = st.text_input("Compareceram (Nome)", value="")
        
        st.markdown("---")
        c1, c2, c3 = st.columns(3)
        temp_9 = c1.number_input("Templo e mezanino", min_value=0, key="t9")
        vis_9 = c2.number_input("Visitantes", min_value=0, key="v9")
        sex_9 = c3.number_input("Sexto andar", min_value=0, key="s9")
        
        st.write("**Servindo (9h):**")
        s1, s2, s3 = st.columns(3)
        dia_9 = s1.number_input("Diaconia", min_value=0, key="d9")
        mes_9 = s2.number_input("Mesa", min_value=0, key="m9")
        lou_9 = s3.number_input("Louvor", min_value=0, key="l9")

        st.write("**MI (9h):**")
        mi1, mi2, mi3 = st.columns(3)
        mi_c_9 = mi1.number_input("Crianças (MI 9h)", min_value=0)
        mi_s_9 = mi2.number_input("Servos (MI 9h)", min_value=0)
        mi_p_9 = mi3.number_input("Pai/Mãe (MI 9h)", min_value=0)

        st.write("**MPA (9h):**")
        mp1, mp2, mp3 = st.columns(3)
        mpa_c_9 = mp1.number_input("Crianças (MPA 9h)", min_value=0)
        mpa_s_9 = mp2.number_input("Servos (MPA 9h)", min_value=0)
        mpa_p_9 = mp3.number_input("Pai/Mãe (MPA 9h)", min_value=0)
        
        ebed_9 = st.number_input("Ebed", min_value=0)

    # --- CULTO 11:00 ---
    with st.expander("📝 DADOS DO CULTO DAS 11:00h", expanded=False):
        resp_11 = st.text_input("Responsável pela contagem (11h)", value="")
        data_11 = st.date_input("Data (11h)", value=None, format="DD/MM/YYYY")
        comp_11 = st.text_input("Compareceram (Nome 11h)", value="")
        
        st.markdown("---")
        c4, c5, c6 = st.columns(3)
        temp_11 = c4.number_input("Templo e mezanino ", min_value=0, key="t11")
        vis_11 = c5.number_input("Visitantes ", min_value=0, key="v11")
        sex_11 = c6.number_input("Sexto andar ", min_value=0, key="s11")
        
        st.write("**Servindo (11h):**")
        s4, s5, s6 = st.columns(3)
        dia_11 = s4.number_input("Diaconia ", min_value=0, key="d11")
        mes_11 = s5.number_input("Mesa ", min_value=0, key="m11")
        lou_11 = s6.number_input("Louvor ", min_value=0, key="l11")

        st.write("**MI (11h):**")
        mi4, mi5, mi6 = st.columns(3)
        mi_c_11 = mi4.number_input("Crianças (MI 11h)", min_value=0)
        mi_s_11 = mi5.number_input("Servos (MI 11h)", min_value=0)
        mi_p_11 = mi6.number_input("Pai/Mãe (MI 11h)", min_value=0)

        st.write("**Classe Batismo (11h):**")
        ba1, ba2, ba3 = st.columns(3)
        bat_j = ba1.number_input("Jovens", min_value=0)
        bat_a = ba2.number_input("Adultos", min_value=0)
        bat_s = ba3.number_input("Servos ", min_value=0)

    # --- CÁLCULOS ---
    total_comp_9 = temp_9 + vis_9 + sex_9
    total_serv_9 = dia_9 + mes_9 + lou_9
    total_mi_9 = mi_c_9 + mi_s_9 + mi_p_9
    total_mpa_9 = mpa_c_9 + mpa_s_9 + mpa_p_9
    total_9h = total_comp_9 + total_serv_9 + total_mi_9 + total_mpa_9 + ebed_9

    total_comp_11 = temp_11 + vis_11 + sex_11
    total_serv_11 = dia_11 + mes_11 + lou_11
    total_mi_11 = mi_c_11 + mi_s_11 + mi_p_11
    total_bat_11 = bat_j + bat_a + bat_s
    total_11h = total_comp_11 + total_serv_11 + total_mi_11 + total_bat_11

    total_geral = total_9h + total_11h

    if st.button("GERAR RELATÓRIO FINAL", use_container_width=True):
        dt9 = data_9.strftime('%d/%m/%Y') if data_9 else ""
        dt11 = data_11.strftime('%d/%m/%Y') if data_11 else ""
        
        relatorio = f"""Relatório dos cultos

Culto das 9:00hrs

Responsável pela contagem: {resp_9}
Data: {dt9}
Compareceram: {comp_9}
Templo e mezanino: {temp_9}
Visitantes: {vis_9}
Sexto andar: {sex_9}
Total: {total_comp_9}

Servindo:
Diaconia: {dia_9}
Mesa: {mes_9}
Louvor: {lou_9}
Total: {total_serv_9}

MI:
Crianças: {mi_c_9}
Servos: {mi_s_9}
Pai/Mãe: {mi_p_9}
Total: {total_mi_9}

MPA:
Crianças: {mpa_c_9}
Servos: {mpa_s_9}
Pai/Mãe: {mpa_p_9}
Total: {total_mpa_9}

Ebed: {ebed_9}

TOTAL DO CULTO DAS 9:00hrs: {total_9h}

--------------------------------------

Culto das 11:00hrs

Responsável pela contagem: {resp_11}
Data: {dt11}
Compareceram: {comp_11}
Templo e mezanino: {temp_11}
Visitantes: {vis_11}
Sexto andar: {sex_11}
Total: {total_comp_11}

Servindo:
Diaconia: {dia_11}
Mesa: {mes_11}
Louvor: {lou_11}
Total: {total_serv_11}

MI
Crianças: {mi_c_11}
Servos: {mi_s_11}
Pai/Mãe: {mi_p_11}
Total: {total_mi_11}

Classe batismo:
Jovens: {bat_j}
Adultos: {bat_a}
Servos: {bat_s}
Total: {total_bat_11}

TOTAL DO CULTO DAS 11:00hrs: {total_11h}

TOTAL GERAL: {total_geral}"""
        
        st.code(relatorio, language="text")
        st.success("Relatório gerado! Copie o texto acima.")

else:
    st.warning("Aguardando senha PIB474...")
