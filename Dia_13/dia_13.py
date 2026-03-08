ataques = [
    {'data': '24/01', 'tipo': 'DDoS', 'origem': 'China'},
    {'data': '25/01', 'tipo': 'Phishing', 'origem': 'Russia'}
]

with open ('relatorio_ataques.csv', 'w') as relatorio:
    relatorio.write(f'Data, Tipo, Origem\n')
    for dados_ataques in ataques:
        relatorio.write(f'{dados_ataques['data']}, {dados_ataques['tipo']}, {dados_ataques['origem']}\n')
