### Dia 20: O Grande Integrador (Log de Auditoria) 🕵️‍♂️

Lucas, chegamos ao final do primeiro terço da mentoria.
Hoje não tem conceito novo. Hoje é **Prova de Fogo**.

Você vai construir um script que une **TUDO** o que aprendeu até agora:

1.  Listas e Loops (Dia 2/5)
2.  Requests e APIs (Dia 18/19)
3.  Tratamento de Erros (Dia 6)
4.  Datetime (Dia 17)
5.  Escrita de Arquivos (Dia 12/13)

**O Cenário:**
Seu chefe te deu uma lista de CEPs misturados (alguns bons, alguns ruins).
Sua missão é auditá-los. Você deve consultar um por um e gerar um arquivo de log chamado `auditoria.txt`.

**Requisitos do Script:**

1.  **Lista:** `ceps = ['20000-000', '99999-999', '01001-000']` (Um inválido no meio).
2.  **Arquivo:** Abra `auditoria.txt` em modo `w` (escrita) ou `a` (append).
3.  **Loop:** Para cada CEP da lista:
      * Pegue a **Hora Agora** (ex: `14:30:01`).
      * Consulte a API.
      * **Se der certo (CEP existe):** Escreva no arquivo: `[HORA] Sucesso: CEP X é Rua Y`.
      * **Se der erro (CEP não existe):** Escreva no arquivo: `[HORA] Falha: CEP X não localizado`.
      * *Importante:* Use o `\n` para pular linha no arquivo.
4.  **Feedback Visual:** Dê um `print` na tela apenas dizendo "Processando CEP X..." para o usuário não achar que travou.

Isso é um script de automação real. Se você fizer isso, você automatiza 50% do trabalho de um assistente administrativo. Valendo\!
