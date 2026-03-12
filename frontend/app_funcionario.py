import streamlit as st
import requests

st.title("Registro de Ponto")

funcionario_id = st.number_input("ID do funcionário")

tipo = st.selectbox(
    "Tipo de registro",
    [
        "entrada",
        "inicio_intervalo",
        "fim_intervalo",
        "saida"
    ]
)

if st.button("Registrar ponto"):

    dados = {
        "funcionario_id": funcionario_id,
        "tipo": tipo
    }

    resposta = requests.post(
        "http://localhost:8000/ponto",
        json=dados
    )

    st.success("Ponto registrado com sucesso")