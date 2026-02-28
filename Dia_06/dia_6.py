lista_clientes = [
    {'id':1, 'nome': 'Lucas', 'ativo': True},
    {'id':2, 'nome': 'Pedro', },
    {'id':3, 'nome': 'Maria', 'ativo': False}
]

for cliente in lista_clientes:
    try:
        if cliente['ativo']:
            print('Cliente Ativo')
        else:
            print('Cliente Inativo')
    except:
        print(f'Erro na identificação do status "ativo"')
        

