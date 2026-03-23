### Dia 23: O Organizador (Módulos e Importação) 📦

Lucas, seu arquivo está ficando gigante.
Classes misturadas com execução, misturadas com imports... Em sistemas reais, isso vira um caos.

Hoje vamos aprender a **Modularização**.
Cada classe deve viver na sua própria "casa" (arquivo). E o arquivo principal (`main.py`) apenas chama elas.

**A Estrutura de Pastas:**
Imagine que você tem 3 arquivos na mesma pasta:

1.  `base.py` (Onde mora o Pai)
2.  `premium.py` (Onde mora o Filho)
3.  `main.py` (Onde você roda o código)

**Como conectar?**
No arquivo `premium.py`, para o filho herdar do pai, ele precisa conhecer o pai:
`from base import AuditorDeCeps`

No arquivo `main.py`, para usar o robô:
`from premium import AuditorDebochado`

**Sua Missão:**
Quebre o seu código perfeito de hoje em **3 arquivos separados**.

1.  **`robo_base.py`**: Coloque a classe `AuditorDeCeps` e os imports necessários (`requests`, `datetime`).
2.  **`robo_filho.py`**: Coloque a classe `AuditorDebochado`.
      * *Atenção:* Você vai precisar fazer `from robo_base import AuditorDeCeps` no topo desse arquivo, senão ele não sabe quem é o Pai.
3.  **`main.py`**:
      * Importe o filho (`from robo_filho import AuditorDebochado`).
      * Crie a lista de CEPs.
      * Instancie e rode o `auditar()`.

Quero ver se você consegue fazer esses arquivos conversarem entre si. Isso é arquitetura de software.
