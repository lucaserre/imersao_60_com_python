### Dia 9: Múltiplos Ingredientes (Argumentos)

Para fechar o caixão da dúvida sobre Funções, vamos fazer algo que seu robô vai precisar muito: **Argumentos Opcionais**.

Até agora seu liquidificador só aceitava 1 coisa (o valor).
Mas e se quisermos configurar a taxa de juros? E se um cliente VIP tiver juros menores?

**Sintaxe:**
Você pode pedir mais de um dado na entrada, separando por vírgula.

```python
def calcular_total(valor, juros):
    total = valor * juros
    return total

# Usando:
cliente_a = calcular_total(100, 1.1) # Juros normal (10%)
cliente_b = calcular_total(100, 1.5) # Agiota (50%)

```

**Seu Desafio:**
Seu script de WhatsApp manda mensagem. Mas a mensagem muda se for "Bom dia", "Boa tarde" ou "Boa noite".

1. Crie uma função `criar_saudacao(nome, periodo)`.
2. Dentro dela, use **f-string** para retornar: "Bom [periodo], Sr(a). [nome]!".
3. Fora da função, chame ela passando `'Lucas'` e `'dia'`.
4. Imprima o resultado.

Quero ver você passar **duas** variáveis diferentes para dentro da caixa mágica.

🛠️ A Minha Solução (verificar somente após a execução do desafio)

```python
def criar_saudacao(nome, periodo):
    cumprimentar = f"Bom {periodo}, Sr(a){nome}"
    return cumprimentar

pessoa_1 = criar_saudacao('Lucas', 'dia')
print(pessoa_1)


