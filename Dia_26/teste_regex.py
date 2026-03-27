import re
from robo_filho import AuditorDebochado

email_suporte = """
Olá Lucas, segue o relato dos clientes de hoje:
O cliente João informou o cep 25725-380, mas a encomenda não chegou.
A Maria disse que mora no 99999-999 e o sistema travou.
Já o Pedro (CPF 123.456.789-00) mandou o cep 01001-000.
Favor auditar.
"""

extracao_conteudo = re.findall(r"\d{5}-\d{3}", email_suporte)

robo_leitor = AuditorDebochado(extracao_conteudo)
robo_leitor.auditar()