# def calcular_multa(valor_original):
#    valor_atualizado = valor_original + 2
#    return valor_atualizado

# boleto = calcular_multa(100)
# print(boleto)

def calcular_multa_errada(valor_original):
    valor_atualizado = valor_original + 2
    print(f"O valor lá dentro é {valor_atualizado}")
    # Note que NÃO tem return aqui. A função termina sem devolver nada.

# Tentando pegar o valor
boleto = calcular_multa_errada(100)

print(f"O valor que eu peguei na mão foi: {boleto}")