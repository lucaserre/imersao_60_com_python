import requests

url = "https://httpbin.org/get"

pesquisa_cliente = {
    'nome' : 'Lucas',
    'idade' : 25,
    'cargo' : 'tech_lead' 
}

busca = requests.get(url, params=pesquisa_cliente, timeout=3)

print(f'URL: {busca.url}  --- JSON: {busca.json()} e busca: {busca}  ')
