### Dia 3: O Fichário (Dicionários)

Até agora usamos **Listas** (`[]`). Listas são ótimas para coisas simples, como uma lista de compras.
Mas para o seu robô de cobrança, uma lista é perigosa.

Imagine que você tem os dados de um cliente numa lista:
`dados = ['Lucas', '2199999999', 'R$ 500,00']`

Se eu perguntar: *"Onde está o telefone?"*
Você tem que lembrar: *"Ah, está na posição 1"*.
Isso é frágil. Se alguém mudar a ordem, seu robô manda dinheiro para o telefone e liga para o valor.

**A Solução: Dicionários (`{}`)**
O Dicionário é a estrutura mais importante do Python (e das APIs que você quer dominar).

**Explicação de 5 Anos:**
A Lista é uma pilha de pratos numerados (0, 1, 2...).
O Dicionário é um **Fichário com etiquetas**. Você não pede "me dê o item 1". Você pede "me dê a ficha do Telefone".

**Sintaxe:**

```python
# Chave (Etiqueta): Valor (O que tem dentro)
cliente = {
    'nome': 'Lucas',
    'status': 'Devedor',
    'divida': 500
}

```

Para pegar o valor, você chama a etiqueta:
`print(cliente['nome'])` -> Sai: "Lucas"

---

### O Desafio do Dia (Estruturando Dados)

Vamos simular uma resposta de API (aquilo que seu robô vai ler no futuro).

Abaixo, crie um **Dicionário** chamado `contrato` que represente você mesmo.
Ele deve ter obrigatoriamente as seguintes **Chaves (Keys)** com os seus dados reais (ou fictícios):

1. `cliente` (String)
2. `parcelas_atraso` (Int)
3. `vip` (Boolean - invente se você é VIP ou não)
4. `telefones` (Aqui está a pegadinha: Quero uma **Lista** com dois números de telefone *dentro* desse valor).

Quero ver se você consegue misturar Dicionário com Lista dentro.

---

### 🛠️ A Minha Solução (resolver antes de visualizar aqui)

Aqui está o script desenvolvido para resolver o desafio:

```python
#criar um dicionário
#alimentar com informações como: cliente, parcelas_atraso_vip e telefones

contrato = {
    'cliente' : 'Lucas',
    'parcelas_atraso' : 2,
    'vip' : True,
    'telefones' : ['3199999-8888', '31 98888-9999']

}

print(contrato['telefones'][1])
