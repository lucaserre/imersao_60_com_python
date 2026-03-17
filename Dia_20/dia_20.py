import datetime
import requests

ceps = ['25725380', '99999-999', '01001-000', '20000-000', '8979797-8000']

def print_e_escreve(mensagem, dados):
    print(mensagem)
    dados.write(mensagem + '\n')
    


with open ('auditoria.txt', 'w', encoding='utf-8') as auditoria:
    
    for verificacao in ceps:
        print(f'Processando CEP: {verificacao}')
        url = f'https://viacep.com.br/ws/{verificacao}/json/'
        busca_cep = requests.get(url)
        hora_agora = datetime.datetime.now()
        relogio = f"{hora_agora.strftime('%H:%M:%S')}"
        


        if busca_cep.status_code == 200:
            localizacao = busca_cep.json()
            
            if 'erro' in localizacao:
                print_e_escreve(f"{relogio} Falha: CEP {verificacao} não localizado", auditoria )
                
                

            else:
                print_e_escreve(f"{relogio} Sucesso: CEP {verificacao} é {localizacao['logradouro']} ", auditoria)
                
        else:
            print_e_escreve(f"{relogio} Formato incorreto ou servidor explodiu", auditoria)
            