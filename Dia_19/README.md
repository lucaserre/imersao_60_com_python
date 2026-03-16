### Dia 19: O Porteiro da Balada (Status Codes) 🛑

Você descobriu na prática que `200` é "Sucesso" e `400` é "Erro".
Mas o seu código atual é "ingênuo". Ele assume que **sempre** vai dar certo.

Se você colocar um CEP que não existe (ex: `99999-999`), a API da ViaCEP devolve um erro. O seu script vai tentar ler `localizacao['logradouro']` de algo que não existe e vai explodir na cara do usuário.

Na Cibersegurança e na Automação, nós **nunca confiamos na API**. Nós checamos a identidade antes de deixar entrar.

**Os Códigos que você precisa decorar:**

* **200:** OK (Deu certo, pode passar).
* **400:** Bad Request (Você mandou dados tortos, tipo o ponto no CEP).
* **404:** Not Found (O endereço não existe).
* **500:** Internal Server Error (O servidor deles pegou fogo, culpa deles).

**Sua Missão:**
Melhore o seu script de CEP. Antes de tentar ler o Bairro ou Logradouro, verifique se a porta abriu.

1. Faça o `requests.get`.
2. Use um `if` para verificar `busca_cep.status_code`.
3. **Se for 200:** Transforme em JSON e imprima o endereço bonito.
4. **Se for diferente de 200:** Imprima "Erro ao consultar API. Código: [o código de erro]".
* *Desafio Extra:* A ViaCEP tem uma pegadinha. Se o CEP tem formato válido mas não existe (ex: 99999-999), ela retorna status 200, mas com um JSON assim: `{'erro': true}`. Tente tratar isso também dentro do sucesso!



Quero ver um código que não quebra nem se a internet cair.
