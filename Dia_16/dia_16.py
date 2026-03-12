import json 
with open('config.json', 'r') as comandos:
    dados = json.load(comandos)

    print(f"Iniciando o robô {dados['nome_robo']}, versão{dados['versao']}. Horários da manhã:{dados['hora_cobranca']['manha']}")