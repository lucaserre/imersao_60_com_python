### Dia 29: O Detetive de Filtros (Query Parameters) e o Botão de Pânico ⏱️

Nós já vimos a URL limpa: `site.com/api`
Mas você já reparou que às vezes o link de um site fica gigante e cheio de pontos de interrogação e sinais de igual?
`site.com/busca?cliente=lucas&status=devedor&cidade=petropolis`

Isso se chama **Query Parameters** (Parâmetros de Consulta). É assim que enviamos filtros via método `GET` sem precisar colocar os dados no "cofre" do `POST`.

Você *poderia* montar essa URL gigante usando `f-string`, mas o `requests` tem um jeito sênior de fazer isso usando dicionários.

E tem mais um detalhe: **O Botão de Pânico (Timeout)**.
Se você mandar o robô consultar o ViaCEP e a internet dos Correios cair, seu script vai ficar travado esperando a resposta **para sempre**. Um script profissional exige um limite de tempo.

**A Sintaxe do Sênior:**

```python
import requests

url_base = "https://httpbin.org/get"

# 1. Criamos os filtros num dicionário limpo
filtros = {
    "cidade": "petropolis",
    "status": "ativo"
}

# 2. Passamos os filtros no 'params' e definimos que ele só pode esperar 5 segundos (timeout)
try:
    resposta = requests.get(url_base, params=filtros, timeout=5)
    print(resposta.url) # Vai imprimir o link montado bonitinho!
except requests.exceptions.Timeout:
    print("O servidor demorou demais para responder. Abortando missão!")
```

### O Desafio do Dia (A Busca Otimizada) 🔍

1.  Crie um script (`teste_query.py`).
2.  Use a URL `https://httpbin.org/get`.
3.  Crie um dicionário de parâmetros chamado `pesquisa_cliente`. Coloque dentro dele:
      * `nome`: "Seu Nome"
      * `idade`: 25 (ou a sua)
      * `cargo`: "tech\_lead"
4.  Faça a requisição `GET` passando os `params=pesquisa_cliente` e um `timeout=3` (3 segundos).
5.  Imprima a URL final gerada pelo Python (`resposta.url`) para você ver a mágica acontecendo.
6.  Imprima o JSON de resposta e procure a chave `"args"`. É ali que o servidor do httpbin guarda o que você enviou.

Bora montar esse filtro e colocar uma trava de segurança no tempo de resposta?
