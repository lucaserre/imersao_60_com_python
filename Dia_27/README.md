### Dia 27: O Crachá de Acesso (API Headers e Autenticação) 🎫

Lucas, até agora nós brincamos no parquinho público. A API do ViaCEP é maravilhosa, mas ela é uma porta aberta na rua. Qualquer um entra, pede um CEP e vai embora.

No mundo corporativo (e no Blue Team), **nenhuma** API útil é aberta. Você precisa provar quem você é. Se você tentar bater na porta da API do GitHub, do Slack, ou do sistema interno da empresa sem se identificar, você toma um Erro `401 (Unauthorized)` ou `403 (Forbidden)` na cara.

Nós fazemos essa identificação através dos **Headers (Cabeçalhos)**.
O Header é o crachá que o seu robô pendura no pescoço antes de bater na porta do servidor.

**A Sintaxe (Como colocar o crachá):**

```python
import requests

# 1. A URL que vamos atacar
url = "https://api.github.com/user"

# 2. O Crachá (Um dicionário simples!)
meus_headers = {
    "Authorization": "Bearer SEU_TOKEN_SECRETO_AQUI",
    "User-Agent": "RoboDoLucas/1.0" # Educado avisar quem é o robô
}

# 3. O requests.get agora leva o crachá junto
resposta = requests.get(url, headers=meus_headers)
```

-----

### O Desafio do Dia (O Teste de Intrusão Autorizado) 🕵️‍♂️

Não vamos criar contas complexas hoje. Vamos usar o **httpbin.org**, que é um site mundialmente famoso construído exatamente para programadores testarem requisições de APIs.

Existe uma rota secreta nele que **só** aceita requisições se você mandar um crachá de "Bearer Token" (um tipo muito comum de token de segurança).

**Sua Missão:**

1.  Crie um script novo (`teste_token.py`).
2.  A URL alvo é: `https://httpbin.org/bearer`
3.  Crie um dicionário chamado `cracha`. Dentro dele, coloque a chave `"Authorization"` e o valor `"Bearer LucasTechLead2026"`. *(Nota: A palavra 'Bearer' tem que estar ali, seguida de um espaço, e depois o seu token inventado).*
4.  Faça o `requests.get()` passando a URL e o parâmetro `headers=cracha`.
5.  Verifique o `status_code`.
      * **Se for 200:** Imprima "Acesso Permitido\!" e imprima o `.json()` da resposta para ver o que o servidor ecoou de volta.
      * **Se for diferente de 200:** Imprima "Acesso Negado\! Faltou o crachá."

**O Teste do Hacker:** Antes de mandar a versão certa, faça o `requests.get(url)` **SEM** o header e mande imprimir o status code, só para você ver com os próprios olhos o servidor te expulsando com um erro 401.

Quero ver você passar pela catraca de segurança\! Would you like me to explain more about the different types of tokens used in cybersecurity after you finish?
