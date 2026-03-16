### Dia 18: O Carteiro (Bibliotecas Externas e PIP)

Lucas, até hoje usamos as ferramentas que vêm "de fábrica" no Python (`json`, `datetime`, `csv`, `random`).
Mas o poder real do Python está no que a comunidade cria.

Para o seu robô falar com a Web (APIs), o Python "puro" é ruim.
Existe uma ferramenta chamada **Requests** que é o padrão mundial. Mas ela não vem instalada.

**Conceito 1: O `pip` (App Store)**
No seu computador pessoal (terminal), para baixar uma ferramenta nova, você usa o comando:
`pip install requests`
*(Aqui no nosso chat eu já tenho ela instalada, mas anote isso para sua vida).*

**Conceito 2: O `requests` (O Navegador Invisível)**
O `requests` finge ser um Google Chrome. Ele acessa um site, pega o código e traz para você.

**Sintaxe:**

```python
import requests

# O .get() é igual digitar o site e dar Enter
resposta = requests.get("https://site.com.br")

print(resposta.status_code) # 200 = OK, 404 = Não achou
print(resposta.json()) # Pega o conteúdo se for JSON

```

---

### O Desafio do Dia (Consultando CEP) 🇧🇷

Seu robô de cobrança precisa validar o endereço do cliente antes de mandar carta.
Vamos usar uma **API Pública Real** (ViaCEP).

**Sua Missão:**

1. Importe `requests`.
2. Defina uma variável com um CEP real (pode ser o seu ou um genérico, ex: `"01001000"` - Praça da Sé). *Use String, não Int, para não perder o zero na frente.*
3. Monte a URL. A API funciona assim: `https://viacep.com.br/ws/[SEU_CEP]/json/`.
* Use **f-string** para enfiar seu CEP no meio do link.


4. Faça o `requests.get()` desse link.
5. Imprima: "Endereço encontrado: [Logradouro], [Bairro] - [Localidade]/[UF]".
* *Dica: O resultado do `.json()` é um dicionário. Você já sabe ler dicionários.*



Quero ver você sair do seu computador e tocar a internet pela primeira vez.
