import streamlit as st
import requests

API = "https://bom-preco-sistema.onrender.com"

st.set_page_config(
    page_title="Sistema Bom Preço",
    layout="wide"
)

st.title("Sistema Bom Preço")

menu = st.sidebar.selectbox(
    "Menu",
    ["Dashboard", "Funcionários", "Folha"]
)

# DASHBOARD
if menu == "Dashboard":

    st.header("Visão Geral")

    res = requests.get(f"{API}/funcionarios")

    if res.status_code == 200:

        funcionarios = res.json()

        st.metric(
            "Total de Funcionários",
            len(funcionarios)
        )


# FUNCIONARIOS
if menu == "Funcionários":

    st.header("Cadastrar Funcionário")

    nome = st.text_input("Nome")
    cpf = st.text_input("CPF")
    cargo = st.text_input("Cargo")
    departamento = st.text_input("Departamento")

    salario = st.number_input("Salário")

    data_admissao = st.date_input("Data de Admissão")

    if st.button("Cadastrar"):

        dados = {
            "nome": nome,
            "cpf": cpf,
            "email": "",
            "telefone": "",
            "cargo": cargo,
            "departamento": departamento,
            "salario": salario,
            "carga_horaria": 44,
            "data_admissao": str(data_admissao)
        }

        res = requests.post(
            f"{API}/funcionarios",
            json=dados
        )

        if res.status_code == 200:

            st.success("Funcionário cadastrado")

    st.subheader("Lista de Funcionários")

    res = requests.get(f"{API}/funcionarios")

    if res.status_code == 200:

        st.table(res.json())


# FOLHA
if menu == "Folha":

    st.header("Criar Folha")

    funcionario_id = st.number_input("ID Funcionário")

    salario = st.number_input("Salário Base")

    extras60 = st.number_input("Hora Extra 60%")
    extras100 = st.number_input("Hora Extra 100%")

    descontos = st.number_input("Descontos")

    if st.button("Gerar Folha"):

        dados = {
            "funcionario_id": funcionario_id,
            "mes": 3,
            "ano": 2026,
            "salario_base": salario,
            "hora_extra_60": extras60,
            "hora_extra_100": extras100,
            "descontos": descontos,
            "liquido": salario
        }

        res = requests.post(
            f"{API}/folha",
            json=dados
        )

        if res.status_code == 200:

            st.success("Folha criada")