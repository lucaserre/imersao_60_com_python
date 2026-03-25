### Dia 25: O Guardião da Execução (`if __name__ == "__main__":`) 🛡️

Lucas, agora que temos arquivos conversando entre si (`import`), existe um **risco invisível**.

Quando você faz `import robo_base`, o Python **lê e executa** tudo o que está dentro daquele arquivo. Se tiver um `print` solto ou um teste perdido lá no meio do `robo_base.py`, ele vai aparecer na tela do `main.py` sem você querer.

Para evitar isso, usamos uma condição especial que verifica: *"Eu estou sendo rodado diretamente ou fui importado?"*

#### O Conceito: A Variável Mágica `__name__`

O Python tem uma etiqueta invisível chamada `__name__`.

| Situação | Valor de `__name__` |
| :--- | :--- |
| Você roda `python robo_base.py` | `"__main__"` (Sou o principal\!) |
| O `main.py` importa o `robo_base` | `"robo_base"` (Sou apenas um módulo) |

Nós usamos isso para criar um **Portão de Segurança**. Código de teste ou execução direta só roda se o arquivo for o principal.

```python
# No fundo do robo_base.py

if __name__ == "__main__":
    # Tudo aqui dentro SÓ roda se você der play NESTE arquivo direto.
    # Se alguém importar esse arquivo, o Python ignora essa parte.
    print("Estou rodando o robo_base.py diretamente para testes!")
    teste = AuditorDeCeps(['00000-000'])
    teste.auditar()
```

-----

### O Desafio do Dia (Blindando os Módulos)

Vamos proteger seus arquivos para que eles sejam duplamente úteis: funcionem como **biblioteca** (importados) e como **script** (rodados sozinhos para teste).

**Sua Missão:**

1.  Abra o `robo_base.py`.
2.  No final do arquivo, adicione o bloco `if __name__ == "__main__":`.
3.  Dentro desse bloco, coloque um código simples de teste (crie uma instância do `AuditorDeCeps` com um CEP qualquer e mande auditar).
4.  **O Teste Real:**
      * Rode o `robo_base.py` direto. O teste deve aparecer.
      * Rode o `main.py`. O teste do `robo_base` **NÃO** deve aparecer (apenas o do `main`).

Quero ver você controlar quem pode falar e quando. Mãos à obra\!
