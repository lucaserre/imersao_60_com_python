### Dia 28: A Transportadora de Valores (O método POST) 🚚

Até agora, você só usou o `requests.get()`.
O `GET` é como ler a vitrine de uma loja. Você pede para ver e o servidor te mostra. Mas você não altera nada lá dentro.

Mas e se você precisar **enviar** um formulário? E se a Débora te pedir para registrar no sistema central da cobrança que um cliente acabou de renegociar uma dívida? Você não pode usar o `GET`. Você precisa **escrever** no banco de dados deles.

Para isso, usamos o `requests.post()`.
O `POST` é um carro-forte. Ele pega um pacote de dados (um JSON), esconde na caçamba (o "Body" da requisição) e entrega no servidor. Na Cibersegurança, é o `POST` que os atacantes usam para tentar enviar senhas num ataque de Força Bruta.

**A Sintaxe do Carro-Forte:**

```python
import requests

url_sistema = "https://httpbin.org/post" # Rota feita para testar POST

# 1. Preparamos a carga (Nosso velho amigo Dicionário)
carga_dados = {
    "cliente": "João da Silva",
    "status": "pago",
    "valor_recuperado": 1500.50
}

# 2. Enviamos o POST. Note que usamos 'json=' em vez de 'headers='
resposta = requests.post(url_sistema, json=carga_dados)

print(f"Status: {resposta.status_code}")
```

-----

### O Desafio do Dia (O Disparo do Alerta) 🚨

Vamos simular o envio de dados do seu robô para um sistema externo de monitoramento.

**Sua Missão:**

1.  Crie o arquivo `teste_post.py`.
2.  A URL alvo será: `https://httpbin.org/post`
3.  Crie um dicionário chamado `alerta_cobranca`. Coloque pelo menos 3 chaves nele (ex: `id_cliente`, `motivo`, `risco`). Invente os valores que quiser.
4.  Faça o `requests.post()` enviando o seu dicionário no parâmetro `json=...`.
5.  Imprima o `status_code` (deve ser 200).
6.  **Importante:** Imprima também o `resposta.json()`. Como o httpbin é um site de eco, ele vai te devolver um espelho mostrando exatamente como o pacote chegou lá do outro lado.

Se você dominar o `POST`, você tem as ferramentas para integrar qualquer automação de envio de mensagens ou atualização de sistemas.

Quer tentar montar essa carga e enviar para o servidor?
