divida = 100


def aplicar_juros(valor):
    com_juros = valor * 1.1
    return com_juros


valor_a_pagar = aplicar_juros(divida) - 5
print(valor_a_pagar)

