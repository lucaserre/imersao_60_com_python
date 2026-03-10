# import csv

# ataques = [
#     {'data': '24/01', 'tipo': 'DDoS', 'origem': 'China'},
#     {'data': '24/01', 'tipo': 'Phishing', 'origem': 'Russia'}
# ]

# with open('relatorio_pro.csv', 'w', newline='') as arquivo:
#     campos = ['data', 'tipo', 'origem']
#     escritor = csv.DictWriter(arquivo, fieldnames=campos)
#     escritor.writeheader()
#     escritor.writerows(ataques)

import csv


funcionarios = [
    {'nome': 'Lucas', 'cargo': 'Tech Lead', 'horas': 160},
    {'nome': 'João', 'cargo': 'Estagiário', 'horas': 100}
 ]

with open('folha_ponto.csv', 'w', newline='') as banco_horas:

    campos = ['nome', 'cargo', 'horas']
    
    escritor = csv.DictWriter(banco_horas, fieldnames=campos)

    escritor.writeheader()

    escritor.writerows(funcionarios)