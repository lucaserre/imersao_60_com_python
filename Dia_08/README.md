# Dia 08: A Corrente (Usando o Retorno na Prática) 🔗

Em automação real, funções raramente usam `print()`. O trabalho de uma função é processar um dado e **devolver** (`return`) um resultado para que o script principal continue trabalhando com ele. É uma linha de montagem.

### 🧠 A Explicação de 5 Anos
Imagine que a sua função é um avaliador de penhores. Você entrega um relógio (o Argumento) na mão dele. Ele entra numa sala fechada, avalia e volta te entregando um papel com o valor (o `return`). Se ele apenas gritasse o valor lá de dentro da sala (`print`), você ouviria, mas não teria o papel em mãos para entregar no caixa. O `return` coloca o dado físico na sua mão para a próxima etapa.

---

### 🎯 O Desafio do Dia (Cálculo em Cadeia)

**Cenário de Negócio:**
Calcular o valor final de uma cobrança. A regra exige aplicar 10% de juros sobre o valor original e, após o acréscimo, aplicar um desconto fixo de R$ 5,00 para incentivar o pagamento.

**A Missão:**
Criar uma função isolada apenas para o cálculo de juros e, fora dela, encadear o resultado retornado com a matemática do desconto.

---

### 🛠️ A Minha Solução (verificar somente após a execução do desafio)

```python
divida = 100

# Função focada em uma única responsabilidade: aplicar juros e devolver o valor
def aplicar_juros(valor):
    com_juros = valor * 1.1
    return com_juros

# Composição: Pegamos o retorno da função e subtraímos 5 na mesma linha
valor_a_pagar = aplicar_juros(divida) - 5

print(f"O valor final a pagar é: R$ {valor_a_pagar:.2f}")
