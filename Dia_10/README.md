### Dia 10: As Ferramentas Prontas (Import e Bibliotecas)

Queridones, parabéns. Você completou a **Fase 1 (Lógica Básica)**.
Você sabe: Variáveis, Tipos, If/Else, Loops, Listas, Dicionários e Funções.
Isso é 80% do que um programador usa.

Agora vamos para a **Fase 2: O Mundo Real**.
No trabalho, você não recria a roda. Você usa ferramentas prontas.
No Python, chamamos isso de **Bibliotecas (Libraries)** ou **Módulos**.

Lembra que no seu primeiro script você disse que usava uma "pausa aleatória" pro WhatsApp não bloquear?
Você não precisa criar a matemática da aleatoriedade. Alguém já criou.

**O Comando `import`:**
É como ir na caixa de ferramentas e pegar uma ferramenta específica que não vem no bolso.

```python
import time  # Importa a ferramenta de TEMPO
import random # Importa a ferramenta de ALEATORIEDADE

print("Vou dormir...")
time.sleep(2) # Dorme por 2 segundos
print("Acordei!")

```

**Seu Desafio:**
Simule o comportamento do seu Robô de WhatsApp.

1. Importe `random` e `time`.
2. Crie uma lista com 3 nomes de clientes.
3. Faça um Loop (`for`) para percorrer a lista.
4. Para cada cliente:
* Imprima "Enviando mensagem para [Nome]..."
* Gere um número aleatório entre 1 e 5 (Use `random.randint(1, 5)`).
* Faça o código "dormir" (`time.sleep`) por esse tempo aleatório.
* Imprima "Mensagem enviada! Esperei X segundos."



Quero ver você controlar o tempo.

***🛠️ A Minha Solução (verificar somente após a execução do desafio)***

```python

import time
import random

lista_clientes = ['Isadora', 'Helen', 'Lucas']

for envio_msg in lista_clientes:
    print (f'Enviando mensagem para {envio_msg}')
    delay = random.randint(1, 5)
    time.sleep(delay)
   
    print(f'Mensagem enviada com sucesso, com delay de {delay} segundos! ')
