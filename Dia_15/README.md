### Dia 15: A Língua da Internet (JSON)

Lucas, chegamos na metade do curso. O CSV é o rei do Excel (Setor Financeiro).
Mas o **Rei da Programação e da Segurança** é o **JSON** (JavaScript Object Notation).

99% das APIs que você vai atacar (Blue/Red Team) ou construir, conversam em JSON.
A boa notícia? **JSON é idêntico a um Dicionário Python.** É literalmente a mesma cara.

A diferença é:

* **Dicionário:** Vive na memória RAM do Python. Se desligar o PC, some.
* **JSON:** É um arquivo de texto ou uma string que viaja pela internet.

Precisamos aprender a transformar um no outro.

* `json.dump()`: Dicionário -> Arquivo JSON (Salvar)
* `json.load()`: Arquivo JSON -> Dicionário (Ler)

**O Desafio do Dia (Arquivo de Configuração):**

Todo software sério tem um arquivo `config.json` para guardar senhas, cores e preferências.
Sua missão é criar o arquivo de configuração do seu Robô.

1. Importe a biblioteca `json`.
2. Crie um dicionário complexo (com listas dentro):
```python
configuracao = {
    'nome_robo': 'Cobrador_v1',
    'versao': 1.5,
    'horarios_permitidos': [9, 10, 11, 14, 15, 16],
    'admin_email': 'lucas@tech.com'
}

```


3. Use o `with open` para criar o arquivo `config.json` (modo `'w'`).
4. Use `json.dump(configuracao, arquivo, indent=4)`.
* *Dica: O `indent=4` serve para o arquivo ficar bonitinho, indentado, e não uma linha única horrível.*



Quero ver você salvar a alma do seu robô num arquivo.
