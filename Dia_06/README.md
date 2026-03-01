### Dia 6: O Mundo Real Quebra (Tratamento de Erros)

Padawan, você está confiante. O script roda, o loop funciona.
Mas no mundo corporativo, **o dado nunca vem limpo**.

Imagine que o estagiário cadastrou um cliente novo no banco de dados, mas **esqueceu de colocar o campo 'ativo'**.
O seu dicionário chegou assim: `{'id': 4, 'nome': 'Pedro', 'email': 'pedro@bol.com'}`.

Se o seu código rodar `if cliente['ativo']` nesse dicionário... **BOOM**.
O Python vai travar com um erro chamado `KeyError` (Chave não encontrada) e seu robô de cobrança vai parar no meio da madrugada.

**Desafio do Dia:**
Como podemos proteger o código?
Existe um comando chamado `try` (tente) e `except` (se der erro, faça isso).

**Sua Missão:**

1. Copie a lista abaixo (que tem um erro proposital no Pedro).
2. Use o `for` normal.
3. Tente (`try`) verificar se ele é ativo e imprimir.
4. Se der erro (`except`), imprima apenas: "Erro no cadastro do cliente [Nome do Cliente]". O código **não pode parar**. Ele tem que continuar para o próximo.

**Dados:**

```python
lista_clientes = [
    {'id': 1, 'nome': 'Lucas', 'ativo': True},
    {'id': 2, 'nome': 'Pedro'},  # Faltou o 'ativo'! Isso quebraria seu código antigo.
    {'id': 3, 'nome': 'Maria', 'ativo': False}
]

```

Quero ver você blindar esse script.








### 🛠️ A Minha Solução (verificar somente após a execução do desafio)

Aqui está o script desenvolvido para resolver o desafio:

```python

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
        

