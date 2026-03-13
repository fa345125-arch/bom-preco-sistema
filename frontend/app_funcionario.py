import streamlit as st
import requests

API = "https://bom-preco-sistema.onrender.com"

st.title("Sistema Bom Preço")

menu = st.sidebar.selectbox(
    "Menu",
    ["Dashboard", "Funcionários"]
)

# DASHBOARD
if menu == "Dashboard":

    st.header("Visão Geral")

    res = requests.get(f"{API}/funcionarios")

    if res.status_code == 200:
        funcionarios = res.json()

        st.metric(
            label="Total de Funcionários",
            value=len(funcionarios)
        )


# FUNCIONARIOS
if menu == "Funcionários":

    st.header("Cadastro de Funcionário")

    nome = st.text_input("Nome")
    cargo = st.text_input("Cargo")
    salario = st.number_input("Salário")

    if st.button("Cadastrar"):

        dados = {
            "nome": nome,
            "cargo": cargo,
            "salario": salario
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