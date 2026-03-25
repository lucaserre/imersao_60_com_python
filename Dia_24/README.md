### Dia 24: O Laboratório Estéril (Virtual Environments) 🧪

Lucas, agora temos um problema invisível.
Você instalou o `requests` no seu computador global (no sistema principal).

Imagine o seguinte cenário de pesadelo:

1.  Hoje, seu **Robô 1** usa `requests` versão 2.0.
2.  Amanhã, você cria um **Robô 2** que *precisa* da `requests` versão 3.0 (que mudou tudo e quebra o código antigo).
3.  Se você atualizar o `requests` no seu PC, **o Robô 1 para de funcionar**.
4.  Se você não atualizar, **o Robô 2 não funciona**.

Você entrou no **Inferno das Dependências** (Dependency Hell). 🔥

**A Solução: Ambientes Virtuais (`venv`)**
No Python, nós criamos uma "bolha" isolada para cada projeto.

  * O Projeto A tem a biblioteca X versão 1.
  * O Projeto B tem a biblioteca X versão 2.
  * Eles não se enxergam. O computador global nem sabe que eles existem.

Isso é **Higiene de Segurança**. No Blue Team, você testa malwares em ambientes isolados. No Python, é igual.

-----

### O Desafio do Dia (Criando a Bolha)

Vamos criar um ambiente isolado para o seu projeto de Auditoria.

**Passo 1: Criar o Venv**
Abra o seu terminal (CMD ou PowerShell ou Terminal do VS Code) **dentro da pasta** onde estão seus scripts (`robo_base.py`, etc).
Digite:

```bash
python -m venv venv
```

*(Tradução: Python, execute o módulo `venv` e crie uma pasta chamada `venv` aqui).*

Você vai ver surgir uma pasta nova chamada `venv` (ou `.venv`). Ela contém uma cópia mini do Python só para esse projeto.

**Passo 2: Ativar a Bolha**
O Windows precisa saber que você quer usar esse Python, e não o global.

  * **No Windows:** `venv\Scripts\activate`
  * **No Mac/Linux:** `source venv/bin/activate`

Se der certo, vai aparecer um `(venv)` verde na frente da linha do terminal. Isso significa: **"Você está dentro da Matrix"**.

**Passo 3: A Prova Real**
Agora que você está na bolha, digite:
`pip list`

Você vai ver que a lista está quase vazia\! **O `requests` sumiu\!** 😱
Isso é ótimo. Significa que estamos num ambiente limpo.

**Sua Missão:**

1.  Crie e ative o `venv`.
2.  Instale o `requests` **dentro da bolha** (`pip install requests`).
3.  Rode seu `main.py` para garantir que tudo funciona.
4.  Gere um arquivo de requisitos (a lista de compras do projeto) com o comando:
    `pip freeze > requirements.txt`

Quero ver você me mandar o conteúdo desse arquivo `requirements.txt`. É assim que você prova para outro programador quais ferramentas seu robô precisa para viver.
