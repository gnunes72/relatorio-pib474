import streamlit as st
from datetime import date

# Configuração da página
st.set_page_config(page_title="Relatório de Cultos", page_icon="⛪", layout="centered")

# --- SISTEMA DE SENHA SIMPLES ---
SENHA_CORRETA = "igreja123" # <--- ALTERE SUA SENHA AQUI

st.sidebar.title("🔐 Acesso Restrito")
senha_digitada = st.sidebar.text_input("Digite a senha para liberar o formulário:", type="password")

if senha_digitada == SENHA_CORRETA:
    st.sidebar.success("Acesso Liberado!")
    
    st.title("⛪ Registro de Cultos")
    st.write("Preencha os campos abaixo para gerar o relatório formatado.")

    # --- ENTRADA DE DADOS: 9:00h ---
    with st.expander("📊 CLIQUE AQUI: Dados do Culto das 09:00h", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            resp_9 = st.text_input("Responsável (9h)", value="Giovane")
            data_9 = st.date_input("Data do Relatório", date.today())
            templo_9 = st.number_input("Templo e Mezanino (9h)", min_value=0, step=1)
            visitantes_9 = st.number_input("Visitantes (9h)", min_value=0, step=1)
            sexto_9 = st.number_input("Sexto Andar (9h)", min_value=0, step=1)
        with col2:
            diaconia_9 = st.number_input("Diaconia (9h)", min_value=0, step=1)
            mesa_9 = st.number_input("Mesa (9h)", min_value=0, step=1)
            louvor_9 = st.number_input("Louvor (9h)", min_value=0, step=1)
        
        st.markdown("---")
        st.subheader("Crianças e Apoio (9h)")
        c1, c2, c3 = st.columns(3)
        mi_c_9 = c1.number_input("MI Crianças", min_value=0, key="mic9")
        mi_s_9 = c2.number_input("MI Servos", min_value=0, key="mis9")
        mi_p_9 = c3.number_input("MI Pais", min_value=0, key="mip9")
        
        ca1, ca2, ca3 = st.columns(3)
        mpa_c_9 = ca1.number_input("MPA Crianças", min_value=0, key="mpac9")
        mpa_s_9 = ca2.number_input("MPA Servos", min_value=0, key="mpas9")
        mpa_p_9 = ca3.number_input("MPA Pais", min_value=0, key="mpap9")

    # --- ENTRADA DE DADOS: 11:00h ---
    with st.expander("📊 CLIQUE AQUI: Dados do Culto das 11:00h", expanded=False):
        col3, col4 = st.columns(2)
        with col3:
            resp_11 = st.text_input("Responsável (11h)", value="Giovane")
            templo_11 = st.number_input("Templo e Mezanino (11h)", min_value=0, step=1)
            visitantes_11 = st.number_input("Visitantes (11h)", min_value=0, step=1)
            sexto_11 = st.number_input("Sexto Andar (11h)", min_value=0, step=1)
        with col4:
            diaconia_11 = st.number_input("Diaconia (11h)", min_value=0, step=1)
            mesa_11 = st.number_input("Mesa (11h)", min_value=0, step=1)
            louvor_11 = st.number_input("Louvor (11h)", min_value=0, step=1)
        
        st.markdown("---")
        st.subheader("Crianças (11h)")
        ci1, ci2, ci3 = st.columns(3)
        mi_c_11 = ci1.number_input("MI Crianças ", min_value=0, key="mic11")
        mi_s_11 = ci2.number_input("MI Servos ", min_value=0, key="mis11")
        mi_p_11 = ci3.number_input("MI Pais ", min_value=0, key="mip11")

    # --- CÁLCULOS LÓGICOS ---
    total_comp_9 = templo_9 + visitantes_9 + sexto_9
    total_serv_9 = diaconia_9 + mesa_9 + louvor_9
    total_mi_9 = mi_c_9 + mi_s_9 + mi_p_9
    total_mpa_9 = mpa_c_9 + mpa_s_9 + mpa_p_9
    total_culto_9 = total_comp_9 + total_serv_9 + total_mi_9 + total_mpa_9

    total_comp_11 = templo_11 + visitantes_11 + sexto_11
    total_serv_11 = diaconia_11 + mesa_11 + louvor_11
    total_mi_11 = mi_c_11 + mi_s_11 + mi_p_11
    total_culto_11 = total_comp_11 + total_serv_11 + total_mi_11

    total_geral = total_culto_9 + total_culto_11

    # --- BOTÃO GERAR RELATÓRIO ---
    st.markdown("### 📋 Resultado Final")
    if st.button("GERAR TEXTO PARA WHATSAPP", use_container_width=True):
        relatorio = f"""Relatório dos cultos

Culto das 9:00hrs
Responsável pela contagem: {resp_9}
Data: {data_9.strftime('%d/%m/%Y')}
Compareceram: {resp_9}
Templo e mezanino: {templo_9}
Visitantes: {visitantes_9}
Sexto andar: {sexto_9}
Total: {total_comp_9}

Servindo:
Diaconia: {diaconia_9} | Mesa: {mesa_9} | Louvor: {louvor_9}
Total: {total_serv_9}

MI:
Crianças: {mi_c_9} | Servos: {mi_s_9} | Pai/Mãe: {mi_p_9}
Total: {total_mi_9}

MPA:
Crianças: {mpa_c_9} | Servos: {mpa_s_9} | Pai/Mãe: {mpa_p_9}
Total: {total_mpa_9}

TOTAL DO CULTO DAS 9:00hrs: {total_culto_9}

--------------------------------------

Culto das 11:00hrs
Responsável pela contagem: {resp_11}
Data: {data_9.strftime('%d/%m/%Y')}
Compareceram: {resp_11}
Templo e mezanino: {templo_11}
Visitantes: {visitantes_11}
Sexto andar: {sexto_11}
Total: {total_comp_11}

Servindo:
Diaconia: {diaconia_11} | Mesa: {mesa_11} | Louvor: {louvor_11}
Total: {total_serv_11}

MI:
Crianças: {mi_c_11} | Servos: {mi_s_11} | Pai/Mãe: {mi_p_11}
Total: {total_mi_11}

TOTAL DO CULTO DAS 11:00hrs: {total_culto_11}

TOTAL GERAL: {total_geral}"""

        st.code(relatorio, language="text")
        st.success("Cópia o texto acima e cole no WhatsApp!")

elif senha_digitada == "":
    st.info("Por favor, digite a senha na barra lateral para acessar o sistema.")
else:
    st.error("Senha incorreta. Acesso negado.")
