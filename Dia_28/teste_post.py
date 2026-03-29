import requests

url = "https://httpbin.org/post"

alerta_cobranca = {
    'id_cliente' : '475',
    'dia_vencimento' : '15',
    'valor_parcela' : 390.05, 
    'forma_pagamento' : 'boleto'
}


retorno = requests.post(url, json=alerta_cobranca)

print(f'O código do status foi: {retorno.status_code} e a resposta JSON do request foi: {retorno.json()}')