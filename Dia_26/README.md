### Dia 26: O Bisturi de Dados (Expressões Regulares - Regex) 🔪

Lucas, seu robô está perfeito. Mas no mundo real da Cibersegurança (Blue Team), a vida não te entrega uma lista limpinha de CEPs ou IPs assim: `['25725380', '99999-999']`.

A vida te entrega um log de servidor de 10.000 linhas, ou um e-mail bagunçado do cliente reclamando, e você tem que **extrair** a informação no meio do lixo.

Para isso, usamos a biblioteca `re` (Regular Expressions).
Regex é como um **Ctrl+F com superpoderes**. Em vez de procurar uma palavra exata, você procura um **Padrão** (ex: "Procure qualquer coisa que tenha 5 números, um traço, e 3 números").

**A Sintaxe do Padrão (Magia Negra):**

  * `\d`: Significa "qualquer dígito" (0-9).
  * `{5}`: Significa "exatamente 5 vezes".
  * `-`: O traço literal.
  * Então, `\d{5}-\d{3}` é o padrão exato de um CEP brasileiro\!

**Como o Python usa isso:**

```python
import re

texto_sujo = "O cep da empresa é 01001-000, mas o do chefe é 20000-000. Ligar no 0800."

# findall = Encontre todos que combinam com esse padrão
lista_limpa = re.findall(r"\d{5}-\d{3}", texto_sujo)

print(lista_limpa) # Saída: ['01001-000', '20000-000']
```

*Nota: Aquele `r` antes das aspas (`r"..."`) significa "Raw String". Diz pro Python não tentar entender as barras invertidas como comandos normais.*

-----

### O Desafio do Dia (O Minerador de Logs)

Você acabou de receber um log de atendimento por e-mail da equipe de suporte. Eles querem que você passe esses CEPs no seu Robô Auditor. O problema? O texto está um nojo.

**O Texto:**

```python
email_suporte = """
Olá Lucas, segue o relato dos clientes de hoje:
O cliente João informou o cep 25725-380, mas a encomenda não chegou.
A Maria disse que mora no 99999-999 e o sistema travou.
Já o Pedro (CPF 123.456.789-00) mandou o cep 01001-000.
Favor auditar.
"""
```

**Sua Missão:**

1.  Crie um script temporário (pode ser `teste_regex.py`).
2.  Importe o `re`.
3.  Use o `re.findall()` com a fórmula de CEP para extrair uma lista limpa a partir desse texto sujo.
4.  **O Grande Final:** Importe o seu `AuditorDebochado` do `robo_filho`, entregue essa lista limpa recém-extraída para ele, e mande ele auditar\!

Quero ver você juntar o Bisturi com a Fábrica. Você topa o desafio ou quer que eu explique mais sobre como o Regex funciona por baixo dos panos?
