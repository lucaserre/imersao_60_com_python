### Dia 11: Saindo da Caixa de Areia (Lendo Arquivos)

Lucas, hora de virar gente grande.
Até agora, seus clientes estavam numa lista dentro do código: `lista = ['Lucas', ...]`.
Isso é brincadeira de criança. Se você tiver 1.000 clientes, você não vai colar 1.000 nomes no código.

No mundo real (e no seu projeto de Cibersegurança), os dados vêm de **Arquivos Externos** (`.txt`, `.csv`, `.log`).

O Python precisa aprender a **Abrir, Ler e Fechar** arquivos do seu computador.

**A Maneira "Burra" (Antiga):**

```python
arquivo = open('clientes.txt', 'r') # 'r' de Read (Ler)
conteudo = arquivo.read()
print(conteudo)
arquivo.close() # Se você esquecer isso, o arquivo trava e ninguém mais mexe.

```

**A Maneira "Tech Lead" (Context Manager):**
Nós usamos o comando `with`. Ele é um mordomo. Ele abre a porta, deixa você fazer a festa, e quando você sai (ou se o código der erro), ele **garante** que a porta fecha sozinha.

```python
# 'with' garante que o arquivo fecha no final
with open('emails.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha)

```

---

### O Desafio do Dia (O Leitor de Logs)

Como futuro Blue Team/SOC, você vai passar a vida lendo logs. Vamos simular isso.

Imagine que você tem um arquivo de texto chamado `servidor.txt` com o seguinte conteúdo (pode criar ele no Bloco de Notas aí ou só fingir que existe):

```text
IP: 192.168.0.1 - OK
IP: 10.0.0.5 - ERRO
IP: 192.168.0.2 - OK

```

**Sua Missão:**

1. Use o `with open` para ler esse arquivo fictício (se não quiser criar o arquivo, me diga como faria o código imaginando que ele existe).
2. Faça um loop linha por linha.
3. **O Pulo do Gato:** Quando o Python lê arquivo, a linha vem com um "enter" invisível no final (`\n`). O `print` dá outro enter. Fica tudo espaçado.
* Use o comando `.strip()` na linha para limpar essa sujeira.


4. Se a linha contiver a palavra "ERRO", imprima: "ALERTA DE SEGURANÇA NA LINHA: [conteúdo da linha]".

Quero ver você minerar texto.
