#preciso de uma lista
#varrer a lista com loop for
#estabelecer uma condição: nomes que começam com 'R'
#imprimir um alerta da condição 
#utilizar nome.startswith('R')


lista_devedores = ['Ana', 'Roberto', 'Carlos', 'Ronaldo', 'Beatriz']

for nome in lista_devedores:
    if nome.startswith('R'):
        print(f'Alerta! O cliente {nome} começa com R')


#Dica Sênior (anote para o futuro): Em produção, a gente 
# "higieniza" o dado antes de testar. if nome.strip().upper().startswith('R'): 
# (Isso remove espaços strip e joga tudo para maiúsculo upper antes de checar. Blindagem total.)