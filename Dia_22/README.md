### Dia 22: O Herdeiro (Herança de Classes) 👑

Lucas, agora que você tem uma classe `AuditorDeCeps`, imagine o seguinte cenário na sua empresa:
O chefe pede um **Auditor Premium**.
Ele faz **tudo** que o auditor normal faz, mas além disso, ele manda um **e-mail** para o gerente se achar um erro grave.

Você vai copiar e colar o código todo de novo? **Jamais.**
Nós usamos a **Herança**.

O "Filho" herda tudo do "Pai" (DNA) e pode ter habilidades extras.

**Sintaxe de 5 Anos:**

```python
# A Classe Pai (que você já fez)
class AuditorDeCeps:
    # ... código antigo ...

# A Classe Filho (Herança)
class AuditorPremium(AuditorDeCeps): # <-- Olha o Pai entre parênteses!
    
    def enviar_email(self):
        print("Enviando email para o chefe...")
```

Quando você criar um `AuditorPremium`, ele já sabe fazer `auditar()` porque herdou do pai. Você não precisa reescrever\!

**Desafio do Dia:**

1.  Pegue o seu código corrigido de hoje (Classe Pai).
2.  Crie uma classe nova `class AuditorDebochado(AuditorDeCeps):`.
3.  Crie um método novo nela chamado `rir_do_erro(self)`.
      * Ele deve imprimir: "HAHAHA CEP ERRADO\!".
4.  **O Desafio de Sobrescrita (Override):**
      * Copie o método `print_e_escreve` para dentro do Filho.
      * Mude ele para que, antes de escrever a mensagem original, ele escreva "--- RELATÓRIO DO ESTAGIÁRIO ---".
      * Isso vai fazer o filho agir diferente do pai.

Quero ver você criar uma dinastia de robôs.
