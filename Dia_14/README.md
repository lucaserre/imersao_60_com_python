### Dia 14: A Bateria Inclusa (`import csv`)

Você "sofreu" para formatar as vírgulas manualmente (`f"{x},{y},{z}"`).
E se o nome da cidade fosse "Washington, D.C."?
O seu código ia ver a vírgula no meio do nome e ia achar que era uma nova coluna. Ia quebrar a tabela inteira.

Para resolver isso, não fazemos na mão. Usamos a biblioteca `csv` do Python. Ela é inteligente e trata essas exceções.

**O Jeito Profissional (`DictWriter`):**
Olha como é muito mais limpo. Você não precisa escrever linha por linha com f-string. Você entrega o dicionário e ele se vira.

```python
import csv

ataques = [
    {'data': '24/01', 'tipo': 'DDoS', 'origem': 'China'},
    {'data': '25/01', 'tipo': 'Phishing', 'origem': 'Russia'}
]

# 1. newline='' é um truque técnico pro Windows não pular linhas extras no CSV
with open('relatorio_pro.csv', 'w', newline='') as arquivo:
    
    # 2. Definimos quem são as colunas (fieldnames)
    campos = ['data', 'tipo', 'origem']
    
    # 3. Criamos o "Escritor Inteligente"
    escritor = csv.DictWriter(arquivo, fieldnames=campos)
    
    # 4. Escreve o cabeçalho sozinho!
    escritor.writeheader()
    
    # 5. Escreve os dados. O writerows (plural) já faz o loop sozinho!
    escritor.writerows(ataques) 

```

---

### Tira-Teima: Decorando o `with open` 🧠

Você disse que esqueceu o `with open` de um dia pro outro. Normal.
Não decore a sintaxe. Decore a **História**:

1. **`with` (Com):** "Com a ajuda do mordomo..."
2. **`open(...)` (Abrir):** "...abra a porta desse arquivo..."
3. **`as` (Como/Apelido):** "...e chame ele de 'arquivo' pra mim."
4. **`:` (Dois pontos):** "Agora faça isso:"

Sempre que esquecer, pense: *"Com abrir arquivo x como y..."* -> `with open(x) as y:`

---

### Desafio do Dia (O Sistema de Ponto)

Seu chefe quer saber as horas trabalhadas dos funcionários.
Você tem os dados brutos em dicionários. Use a biblioteca `csv` que acabei de mostrar para gerar o arquivo final.

**Dados:**

```python
funcionarios = [
    {'nome': 'Lucas', 'cargo': 'Tech Lead', 'horas': 160},
    {'nome': 'João', 'cargo': 'Estagiário', 'horas': 100}
]

```

**Missão:**

1. Importe `csv`.
2. Use `with open` para criar `folha_ponto.csv`.
3. Use `csv.DictWriter` para escrever o cabeçalho e as linhas **sem fazer loop for manual**. Deixe a biblioteca trabalhar por você (`writerows`).

Quero ver o código limpo e sênior.



