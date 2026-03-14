import requests
import json # Sem necessidade de importar o json, porque o requests já o possui importado internamente. 

cep = '25725-380'
url_cep = f'https://viacep.com.br/ws/{cep}/json/'


busca_cep = requests.get(url_cep)
localizacao = busca_cep.json()


    

print(f'Localização encontrada: {localizacao['logradouro']}, {localizacao['bairro']} - {localizacao['localidade']}/{localizacao['uf']}  ')