lista_clientes = [
    {'id': 1, 'nome': 'Lucas', 'email': 'lucas@tse.jus', 'ativo': True},
    {'id': 2, 'nome': 'João', 'email': 'joao@gmail.com', 'ativo': False},
    {'id': 3, 'nome': 'Maria', 'email': 'maria@hotmail.com', 'ativo': True}
]

for cliente in lista_clientes:
    if cliente['ativo'] == True:
        print(f'Enviando email para:', cliente['email'])

# if cliente['ativo'] == True:  # Redundante
#     print(f'Enviando email para:', cliente['email']) # Vírgula fora da f-string

# for cliente in lista_clientes:
#     # 1. Não precisa de "== True". O if já testa se é verdade.
#     # Se 'ativo' for True, ele entra. Se for False, ele pula.
#     if cliente['ativo']:
        
#         # 2. A variável vai DENTRO das chaves da f-string. Fica mais limpo.
#         print(f"Enviando email para: {cliente['email']}")