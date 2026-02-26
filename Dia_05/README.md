### Dia 5: O Chefão da Fase 1 (Lista de Dicionários)

Padawan, chegamos no formato padrão da indústria.
Raramente uma API devolve um só cliente. Ela devolve uma **Lista** cheia de **Dicionários**.

É assim que o Facebook, o Google e o seu sistema de cobrança conversam.

**Estrutura:**
`[ {cliente1}, {cliente2}, {cliente3} ]`

**Desafio Final da Semana:**
Abaixo tem uma lista de clientes. Quero que você crie um script que:

1. Use um **Loop `for**` para ler cliente por cliente (Dia 2).
2. Dentro do loop, use um **`if`** (Dia 1) para verificar se o cliente está `ativo`.
3. SE estiver ativo, imprima: "Enviando email para: [email do cliente]" (Dia 3 e 4).

**Os Dados:**

```python
lista_clientes = [
    {'id': 1, 'nome': 'Lucas', 'email': 'lucas@tse.jus', 'ativo': True},
    {'id': 2, 'nome': 'João', 'email': 'joao@gmail.com', 'ativo': False},
    {'id': 3, 'nome': 'Maria', 'email': 'maria@hotmail.com', 'ativo': True}
]

```

Se você acertar isso, você dominou a base da lógica de programação. Mãos à obra.

### 🛠️ A Minha Solução (verificar somente após a execução do desafio)

Aqui está o script desenvolvido para resolver o desafio:

```python

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

