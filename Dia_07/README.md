### Dia 7: O Liquidificador (Funções `def`)

Lucas, até agora você escreveu scripts que rodam de cima para baixo.
Mas imagine que você precisa calcular juros de boleto em 10 partes diferentes do seu sistema.
Você vai copiar e colar a fórmula de juros 10 vezes? **NÃO.**
Se o juro mudar de 10% para 11%, você teria que mudar em 10 lugares.

**A Solução: Funções (`def`)**
Uma função é um **Eletrodoméstico**.

1. Você constrói ele uma vez (O Liquidificador).
2. Você só joga os ingredientes dentro (Parâmetros).
3. Ele te devolve o resultado pronto (Retorno).

**Sintaxe de 5 Anos:**

```python
# CONSTRUINDO O LIQUIDIFICADOR (Você faz isso uma vez no topo do arquivo)
def liquidificador(fruta):
    suco = f"Suco de {fruta} geladinho"
    return suco  # O 'return' é quando ele te entrega o copo.

# USANDO (Você pode usar mil vezes)
meu_copo = liquidificador("Morango")
print(meu_copo) # Sai: Suco de Morango geladinho

```

---

### O Desafio da Automação (Seu primeiro `def`)

Você vai criar uma função chamada `calcular_multa`.
O seu chefe disse que a multa é fixa: **R$ 2,00** para qualquer boleto atrasado, não importa o valor.

**Sua Missão:**

1. Crie a função `def calcular_multa(valor_original):`.
2. Dentro dela, some 2 reais ao valor.
3. Use o `return` para devolver o valor novo.
4. Fora da função, crie uma variável `boleto = 100` e chame sua função para atualizar esse valor.

Quero ver se você entende a diferença entre *fazer a conta* e *retornar o valor*.

---
---
---


### 🛠️ A Minha Solução (verificar somente após a execução do desafio)

Aqui está o script desenvolvido para resolver o desafio:

```python

def calcular_multa(valor_original):
    valor_atualizado = valor_original + 2
    return valor_atualizado

boleto = calcular_multa(100)
print(boleto)
