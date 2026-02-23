### Dia 2: A Linha de Montagem (Loops `for`)

Em automação, isso é **90% do trabalho**. Você pega uma lista (do Excel, do Banco de Dados) e precisa fazer a mesma coisa para cada item.

**A Explicação de 5 Anos:**
Imagine que você é um caixa de supermercado. O cliente chega com um carrinho cheio (a Lista).
Você não passa o carrinho inteiro no leitor de código de barras.

1. Você pega **um** item.
2. Passa no leitor.
3. Pega o **próximo** item.
4. Repete até o carrinho ficar vazio.

Isso é o **Loop `for**`.

**A Sintaxe (Como se escreve):**

```python
carrinho = ['Maçã', 'Banana', 'Leite']

for item in carrinho:
    print(f"Estou passando o produto: {item}")

```

Traduzindo: "Para cada `item` que estiver dentro de `carrinho`, faça isso..."
A variável `item` é mágica: ela muda de valor a cada volta. Na primeira volta ela vale 'Maçã', na segunda 'Banana'...

---

### O Desafio do Dia (Integrando tudo)

Agora quero ver se você consegue juntar o **Loop** (Dia 2) com o **If** (Dia 1).

**Cenário:**
O Diretor mandou a lista atualizada de devedores. Sua missão é criar um script que varra essa lista e **imprima um alerta APENAS para os nomes que começam com a letra "R"**. Os outros devem ser ignorados silenciosamente.

**Dados:**

```python
lista_devedores = ['Ana', 'Roberto', 'Carlos', 'Ronaldo', 'Beatriz']

```

**Sua missão:**
Escreva o código que percorre essa lista e avisa: "Alerta! O cliente [Nome] começa com R".

*Dica: Lembra do `.startswith('R')` que ensinei ontem?*
