from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

def gerar_recibo(folha, funcionario):

    arquivo = f"recibo_{funcionario.nome}_{folha.mes}_{folha.ano}.pdf"

    styles = getSampleStyleSheet()

    tabela = [
        ["DESCRIÇÃO", "VALOR"],
        ["Salário Base", folha.salario_base],
        ["Hora Extra 60%", folha.hora_extra_60],
        ["Hora Extra 100%", folha.hora_extra_100],
        ["INSS", folha.inss],
        ["Descontos", folha.descontos],
        ["Total Líquido", folha.liquido]
    ]

    elementos = []

    elementos.append(Paragraph("RECIBO DE PAGAMENTO", styles["Title"]))
    elementos.append(Spacer(1,20))

    elementos.append(
        Paragraph(f"Funcionário: {funcionario.nome}", styles["Normal"])
    )

    elementos.append(Spacer(1,20))

    elementos.append(Table(tabela))

    doc = SimpleDocTemplate(arquivo, pagesize=A4)
    doc.build(elementos)

    return arquivo