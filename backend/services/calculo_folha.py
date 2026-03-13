def calcular_folha(salario_base, hora_extra_60, hora_extra_100, adicionais, descontos):

    total_extras = hora_extra_60 + hora_extra_100

    bruto = salario_base + total_extras + adicionais

    inss = bruto * 0.08

    liquido = bruto - inss - descontos

    return {
        "bruto": bruto,
        "inss": inss,
        "liquido": liquido
    }