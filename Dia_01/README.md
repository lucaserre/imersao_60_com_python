# Dia 01: Fundamentos, Lógica e Controle de Fluxo 🚀

O primeiro dia da imersão foi focado em construir a base do raciocínio lógico, entender como o Python armazena dados na memória (Clean Code) e dominar o controle de fluxo (if/else/or/and), aplicando tudo isso no contexto de um bot de cobranças.

---

## 🧠 1. A Lógica por Trás do Robô
**O Desafio:** Explicar a lógica de cobrança de forma simples, sem jargões técnicos.

**A Lógica (Mundo Real):** Imagine que o robô é um carteiro com uma lista mágica. Ele olha para cada nome na lista e faz uma pergunta simples: *"Essa pessoa já pagou o dinheiro do mês?"*. Se a resposta na lista for "Não", ele deixa uma cartinha na caixa de correio dela avisando sobre o atraso. Se a resposta for "Sim", ele sorri, ignora a casa e vai direto para a próxima. Simples, direto e sem perder tempo!

---

## 📦 2. Tipos de Dados (Data Types)
Tradução do filtro do mundo real para como o Python lê na memória:

* **Nome do Cliente** (Ex: "João da Silva") ➡️ `String` (Texto/str)
* **Quantidade de Parcelas** (Ex: 3) ➡️ `Integer` (Número Inteiro/int)
* **Status** (Ex: "Inadimplente") ➡️ `String` (Texto) ou, de forma mais inteligente, um `Boolean` (Verdadeiro ou Falso / True ou False para *is_devedor*).

---

## 🧹 3. Desafio Clean Code (Nomenclatura)
Organizando as "caixas" na memória RAM usando o padrão `snake_case` (boas práticas de mercado):

* ❌ `n` ➡️ ✅ `nome_cliente`
* ❌ `QtdP` ➡️ ✅ `qtd_parcelas`
* ❌ `EhDevedor` ➡️ ✅ `cliente_inadimplente` (ou `is_devedor`)

---

## ⚙️ 4. O Desafio do Controle de Fluxo (O Filtro)
**A Regra:** "Se o cliente deve mais de 3 parcelas E o nome dele começa com 'A', mande mensagem. Senão, ignore."

**A Solução em Python:**
```python
# Dados de teste
parcelas_em_aberto = 5
nome_cliente = 'Aroldo'

def verificar_cobranca():
    # Uso do operador relacional (>), operador lógico (and) e método de string (.startswith)
    if parcelas_em_aberto > 3 and nome_cliente.startswith('A'):
        print(f"Cobrar o cliente {nome_cliente}! Ele deve {parcelas_em_aberto} parcelas.")
    else:
        print("Não cobrar. Ou deve pouco, ou o nome não bate.")

# Rodando a função
verificar_cobranca()
