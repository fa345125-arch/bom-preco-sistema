from reportlab.platypus import SimpleDocTemplate, Table
from reportlab.lib.pagesizes import A4

def gerar_recibo(funcionario):

    arquivo = f"recibo_{funcionario['nome']}.pdf"

    tabela = [
        ["Descrição", "Valor"],
        ["Salário", funcionario["salario"]],
        ["Total Líquido", funcionario["liquido"]]
    ]

    doc = SimpleDocTemplate(arquivo, pagesize=A4)

    elementos = [Table(tabela)]

    doc.build(elementos)

    return arquivo