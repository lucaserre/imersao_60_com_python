import requests


url = f"https://httpbin.org/bearer"

cracha = {
    "Authorization" : "Bearer LucasTechLead2026"
}

autorizacao_api = requests.get(url, headers=cracha)

if autorizacao_api.status_code == 200:
    print(f'Acesso permitido! Response Code:{autorizacao_api.json()}')
else:
    print(f'{autorizacao_api} : Você esqueceu algo, ou não possui autorização!')