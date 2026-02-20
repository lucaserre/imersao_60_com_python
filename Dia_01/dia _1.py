#Desafio ; Imagine que seu chefe chega e diz: "Lucas, se o cliente deve mais 
# de 3 parcelas E o nome dele começa com 'A', mande mensagem. Senão, ignore."

#parcelas_em_aberto = 0
##nome_clientes = ['Aroldo', 'Agustino', 'Roboaldo', 'Filimino', 'Worseley']



#def filtro_de_mensagens():
    #if parcelas_em_aberto == 0:
       # print ('Esse cliente está adimplente')
   # else:
        #print (f'Esse cliente possui {parcelas_em_aberto} em aberto ')

  #  if nome_clientes == (str('%A')):
        #print ('Cobrança pode ser realizada')
    #else:
        #print('Nome do cliente não começa com "A"')



# Dados de teste (Simplificados para UM cliente por enquanto)
#parcelas_em_aberto = 5
#nome_cliente = 'Aroldo'

#def verificar_cobranca():
#    # A REGRA: Maior que 3 parcelas "E" (and) nome começa com 'A'
#    # Perceba o .startswith() -> "Começa com"
#    if parcelas_em_aberto > 3 and nome_cliente.startswith('A'):
#        print(f"Cobrar o cliente {nome_cliente}! Ele deve {parcelas_em_aberto} parcelas.")
#    else:
#        print("Não cobrar. Ou deve pouco, ou o nome não bate.")

# Rodando a função
#verificar_cobranca()
        

hora_atual = 20

if hora_atual > 18 or hora_atual < 8:
    print ('Fora do horário comercial.')
else:
    print ('Loja Aberta: Bem-Vindo!')



