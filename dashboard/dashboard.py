import streamlit as st

st.title("Sistema Bom Preço - Dashboard")

st.header("Indicadores")

funcionarios = 10
pontos_registrados = 120
receitas = 50000
despesas = 32000

saldo = receitas - despesas

st.metric("Funcionários", funcionarios)
st.metric("Pontos registrados", pontos_registrados)
st.metric("Receitas", f"R$ {receitas}")
st.metric("Despesas", f"R$ {despesas}")
st.metric("Saldo", f"R$ {saldo}")