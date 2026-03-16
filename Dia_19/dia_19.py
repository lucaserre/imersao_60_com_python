import requests

cep = '20000-000'
url_cep = f'https://viacep.com.br/ws/{cep}/json/'


busca_cep = requests.get(url_cep)

if busca_cep.status_code == 200:
    localizacao = busca_cep.json()
    if 'erro' in localizacao:
        print(f'Tente verificar se esse realmente é seu cep: {cep}, pois ele não existe')
        
    else:
        print(f"Localização encontrada: {localizacao['logradouro']}, {localizacao['bairro']} - {localizacao['localidade']}/{localizacao['uf']}")
        
            

else:
    print(f'Erro ao consultar API. Código: {busca_cep.status_code}')
