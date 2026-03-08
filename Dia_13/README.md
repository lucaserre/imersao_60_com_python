### Dia 13: O Excel dos Programadores (CSV)

Você aprendeu a lidar com `.txt`. Mas empresas amam planilhas.
Se você mandar um `.txt` pro seu chefe financeiro, ele vai chorar. Se mandar um arquivo que abre no Excel, você é promovido.

Esse formato mágico é o **CSV** (Comma Separated Values - Valores Separados por Vírgula).
É um texto burro, mas que o Excel entende como colunas.

**Estrutura do CSV:**

```text
Nome,Idade,Cargo
Lucas,25,Hacker
Joao,30,Gerente

```

**Sua Missão:**
Você vai criar um relatório de incidentes para a diretoria.

1. Crie uma lista de dicionários (Dia 5) com dados de ataques:
```python
ataques = [
    {'data': '24/01', 'tipo': 'DDoS', 'origem': 'China'},
    {'data': '25/01', 'tipo': 'Phishing', 'origem': 'Russia'}
]

```


2. Abra um arquivo `relatorio_ataques.csv` (modo `'w'`).
3. Primeiro, escreva o cabeçalho manualmente: `"Data,Tipo,Origem\n"`.
4. Faça um loop na lista e escreva os dados separados por vírgula, usando f-string.
* Exemplo de formato: `f"{ataque['data']},{ataque['tipo']},{ataque['origem']}\n"`



Se fizer certo, você poderá abrir esse arquivo no Excel depois. Mãos à obra.


### 🛠️ A Minha Solução (verificar somente após a execução do desafio)

Aqui está o script desenvolvido para resolver o desafio:

```python
ataques = [
    {'data': '24/01', 'tipo': 'DDoS', 'origem': 'China'},
    {'data': '25/01', 'tipo': 'Phishing', 'origem': 'Russia'}
]

with open ('relatorio_ataques.csv', 'w') as relatorio:
    relatorio.write(f'Data, Tipo, Origem\n')
    for dados_ataques in ataques:
        relatorio.write(f'{dados_ataques['data']}, {dados_ataques['tipo']}, {dados_ataques['origem']}\n')
