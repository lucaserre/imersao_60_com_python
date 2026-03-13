import json
import datetime

with open ('config.json', 'r') as comandos:
    dados = json.load(comandos)

    time = datetime.datetime.now()
    relogio = time.hour

    dia_cobranca = dados['hora_cobranca']['noite'] + dados['hora_cobranca']['tarde'] + dados['hora_cobranca']['manha']

    if relogio in dia_cobranca:
        print(f'Hora permitida! Iniciando disparos...')
    else:
        print(f'Repousando. O relógio marca {relogio}')
    

    

    

    

    