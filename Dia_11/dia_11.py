with open ('servidor.txt', 'r') as relatorio:

    for log in relatorio:
        if 'ERRO' in log.strip():
            print(f'ALERTA DE SEGURANÇA NA LINHA {log.strip()} ')
                  