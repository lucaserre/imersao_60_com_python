### Dia 21: A Fábrica de Robôs (Orientação a Objetos - OOP)

Lucas, respire fundo.
Hoje vamos entrar no conceito que separa os scripts (arquivos soltos) dos **Sistemas** (softwares complexos).

Até agora, seu robô é um monte de variáveis (`ceps`, `hora`, `url`) e funções soltas.
E se você precisasse criar **5 robôs diferentes**? Um de cobrança, um de auditoria, um de vendas?
Você ia copiar e colar código 5 vezes? **Não.**

Nós vamos criar uma **CLASSE**.
Uma Classe é uma **Planta (Blueprint)**.
Um Objeto é a **Casa** construída a partir da planta.

**A Analogia de 5 Anos:**

  * **Classe (`class`):** É o molde de plástico da fábrica de brinquedos. O molde não faz nada, ele só define como o brinquedo será.
  * **Objeto (`instance`):** É o boneco que sai da máquina. Você pode fazer 1.000 bonecos iguais usando o mesmo molde.
  * **Atributos (`self.variavel`):** São as características (Cor, Tamanho).
  * **Métodos (`def`):** São os botões do boneco (Falar, Andar).

**Sintaxe Básica:**

```python
class Robo:
    # 1. O Construtor (__init__): O que acontece quando o robô nasce?
    def __init__(self, nome_do_robo):
        self.nome = nome_do_robo # 'self' sou eu mesmo. Guardei meu nome.
        self.bateria = 100
        print(f"Robô {self.nome} foi criado!")

    # 2. Um Método (Ação)
    def dizer_ola(self):
        print(f"Olá, eu sou o {self.nome} e tenho {self.bateria}% de bateria.")

# USANDO A FÁBRICA (Instanciando)
robo1 = Robo("Jarvis") # Nasceu o Jarvis
robo2 = Robo("Ultron") # Nasceu o Ultron (usando o mesmo código!)

robo1.dizer_ola() # Sai: Eu sou Jarvis
robo2.dizer_ola() # Sai: Eu sou Ultron
```

-----

### O Desafio do Dia (Seu Primeiro Objeto)

Vamos transformar seu script de CEP em um **Objeto**.

**Sua Missão:**

1.  Crie uma `class AuditorDeCeps`.
2.  No `__init__`, ele deve receber uma **lista de ceps** e guardar no `self.lista_ceps`.
3.  Crie um método chamado `auditar()`.
      * Mova toda a lógica do seu Loop `for` para dentro desse método.
      * Troque a variável solta `ceps` por `self.lista_ceps`.
4.  **No final do arquivo (fora da classe):**
      * Crie uma lista de CEPs.
      * Instancie o robô: `meu_robo = AuditorDeCeps(lista)`.
      * Mande ele trabalhar: `meu_robo.auditar()`.

*Dica: Importe `requests` e `datetime` lá no topo, como sempre.*

Quero ver você parar de escrever scripts e começar a construir **Componentes**. Boa sorte.
