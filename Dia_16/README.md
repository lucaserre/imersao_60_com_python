### Dia 16: O Robô que Lê (Lendo JSON)

Você criou o cérebro do robô (`config.json`). Agora, precisamos fazer o transplante.
De nada adianta o arquivo existir se o seu script Python não souber ler ele.

No dia a dia de Blue Team ou Automação, você **nunca** deixa senhas ou configurações fixas no código (Hardcode). Você lê de um arquivo. Assim, se a versão mudar, você edita o JSON, não o código.

**A Ferramenta:** `json.load()` (Sem o 's', porque carrega de arquivo).

**Sua Missão:**

1. Crie um novo script (`robo.py`).
2. Importe `json`.
3. Use o `with open` para ler (`'r'`) o arquivo `config.json` que você criou ontem.
4. Carregue o conteúdo para uma variável usando `dados = json.load(arquivo)`.
5. **O Teste Final:** Imprima uma frase complexa acessando os dados lidos:
*"Iniciando o robô [nome_robo] versão [versao]. Horários da manhã: [lista da manhã]"*.

Quero ver você puxar esses dados do arquivo para a tela.
