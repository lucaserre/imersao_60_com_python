### Dia 12: O Escritor (Escrevendo Arquivos)

Você já sabe ler o diário do servidor. Agora você precisa **escrever** o relatório de demissão do estagiário que causou o erro.

Para escrever, mudamos o modo de `'r'` (Read/Ler) para `'w'` (Write/Escrever).

⚠️ **PERIGO MORTAL DO MODO 'W':**
O `'w'` é destrutivo. Se o arquivo já existir e tiver a Bíblia escrita nele, o `'w'` **apaga tudo** e começa do zero numa folha em branco.
*Para adicionar sem apagar (tipo log), usamos o `'a'` (Append), mas hoje vamos usar o `'w'` para criar arquivos novos.*

**Sintaxe:**

```python
with open('relatorio.txt', 'w') as arquivo:
    arquivo.write("Este é o relatório.\n") # \n é o Enter para pular linha
    arquivo.write("O sistema caiu.")

```

**O Desafio do Dia (Gerador de Blacklist):**

Você é do Blue Team. Você detectou 3 IPs maliciosos. Você precisa criar um arquivo chamado `blacklist.txt` para o Firewall ler e bloquear.

1. Crie uma lista no código: `ips_ruins = ['10.0.0.1', '192.168.1.50', '172.16.0.10']`.
2. Abra (crie) o arquivo `blacklist.txt` no modo de escrita (`'w'`).
3. Faça um loop (`for`) na lista.
4. Escreva cada IP no arquivo.
* **Obrigatório:** Adicione um `\n` (pular linha) depois de cada IP, senão eles vão ficar grudados assim: `10.0.0.1192...`. Use f-string: `f"{ip}\n"`.



Quero ver você criar um arquivo real no seu computador agora.

**🛠️ A Minha Solução (verificar somente após a execução do desafio)**

```python

with open ('servidor.txt', 'r') as relatorio:

    for log in relatorio:
        if 'ERRO' in log.strip():
            print(f'ALERTA DE SEGURANÇA NA LINHA {log.strip()} ')
                  
