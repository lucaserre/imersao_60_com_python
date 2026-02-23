hora_atual = 20

# Uso do operador lógico (or) para definir as pontas do horário proibido
if hora_atual > 18 or hora_atual < 8:
    print('Pare! Fora do horário comercial.')
else:
    print('Loja Aberta: Bem-Vindo! Operação de envio permitida.')
