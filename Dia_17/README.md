### Dia 17: O Relógio do Juízo Final (`datetime`) ⏰

Lucas, agora seu robô sabe **QUAIS** são os horários permitidos (9, 10, 11).
Mas ele não sabe que horas são **AGORA**.

Para um robô de automação, saber a hora é crucial. Se ele rodar sábado às 3 da manhã, você é demitido.

Vamos usar a biblioteca `datetime`. Ela é chatinha, mas poderosa.

**O Conceito:**
`datetime.datetime.now()`: Pega a data e hora exata de agora (Ano, Mês, Dia, Hora, Minuto, Segundo, Milissegundo).

**Sua Missão:**

1. Importe `datetime` (além do `json`).
2. Carregue os horários permitidos do seu `config.json` (igual você já fez).
3. Descubra a hora atual. Use: `agora = datetime.datetime.now()`.
4. Extraia **só a hora** (número inteiro) desse horário. Use: `hora_atual = agora.hour`.
5. **A Lógica Final:** Crie um `if`.
* SE a `hora_atual` estiver DENTRO (`in`) da lista de horários da manhã...
* Imprima: "Hora permitida! Iniciando disparos..."
* SENÃO (`else`):
* Imprima: "Robô em repouso. Hora atual: [hora_atual]"



Quero ver você conectar o arquivo JSON com o relógio do sistema.
