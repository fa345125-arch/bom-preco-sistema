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
    [
        "Dashboard",
        "Funcionários",
        "Financeiro",
        "Ponto",
        "Férias"
    ]
)

# =====================
# DASHBOARD
# =====================

if menu == "Dashboard":

    st.header("Visão Geral")

    col1, col2 = st.columns(2)

    funcionarios = requests.get(f"{API}/funcionarios").json()

    with col1:
        st.metric(
            "Funcionários",
            len(funcionarios)
        )

    transacoes = requests.get(f"{API}/transacoes").json()

    entradas = sum(t["valor"] for t in transacoes if t["tipo"] == "entrada")
    saidas = sum(t["valor"] for t in transacoes if t["tipo"] == "saida")

    with col2:
        st.metric(
            "Saldo",
            entradas - saidas
        )


# =====================
# FUNCIONARIOS
# =====================

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

        requests.post(
            f"{API}/funcionarios",
            json=dados
        )

        st.success("Funcionário cadastrado")

    st.subheader("Lista")

    funcionarios = requests.get(
        f"{API}/funcionarios"
    ).json()

    st.table(funcionarios)


# =====================
# FINANCEIRO
# =====================

if menu == "Financeiro":

    st.header("Registrar Transação")

    descricao = st.text_input("Descrição")
    valor = st.number_input("Valor")
    tipo = st.selectbox("Tipo", ["entrada", "saida"])

    if st.button("Registrar"):

        dados = {
            "descricao": descricao,
            "valor": valor,
            "tipo": tipo
        }

        requests.post(
            f"{API}/transacoes",
            json=dados
        )

        st.success("Transação registrada")

    st.subheader("Transações")

    transacoes = requests.get(
        f"{API}/transacoes"
    ).json()

    st.table(transacoes)


# =====================
# PONTO
# =====================

if menu == "Ponto":

    st.header("Registrar Ponto")

    funcionario_id = st.number_input("ID Funcionário")

    if st.button("Entrada"):

        requests.post(
            f"{API}/ponto",
            json={
                "funcionario_id": funcionario_id,
                "tipo": "entrada"
            }
        )

        st.success("Entrada registrada")

    if st.button("Saída"):

        requests.post(
            f"{API}/ponto",
            json={
                "funcionario_id": funcionario_id,
                "tipo": "saida"
            }
        )

        st.success("Saída registrada")


# =====================
# FÉRIAS
# =====================

if menu == "Férias":

    st.header("Registrar Férias")

    funcionario_id = st.number_input("Funcionário ID")
    inicio = st.date_input("Início")
    fim = st.date_input("Fim")

    if st.button("Registrar"):

        requests.post(
            f"{API}/ferias",
            json={
                "funcionario_id": funcionario_id,
                "inicio": str(inicio),
                "fim": str(fim)
            }
        )

        st.success("Férias registradas")