from datetime import datetime


def analisar_jornada(entrada, saida):

    entrada = datetime.fromisoformat(entrada)
    saida = datetime.fromisoformat(saida)

    horas_trabalhadas = (saida - entrada).total_seconds() / 3600

    risco = None

    if horas_trabalhadas > 10:
        risco = "Jornada acima de 10 horas"

    return {
        "horas_trabalhadas": horas_trabalhadas,
        "risco": risco
    }