import requests
import datetime


class AuditorDeCeps:

    def __init__(self, ceps_recebidos):

        self.lista_localizacao = ceps_recebidos


    def print_e_escreve(self, mensagem, arquivo_destino):
        print(mensagem)
        arquivo_destino.write(mensagem + '\n')


    def rir_do_erro(self):
        pass 

    def auditar(self):
        with open('auditoria_robo.txt', 'w', encoding='utf-8') as log:
            

            for verificacao in self.lista_localizacao:
                print(f'Processando CEP: {verificacao}')
                
                url = f'https://viacep.com.br/ws/{verificacao}/json/'
                busca_cep = requests.get(url)
                
                hora_agora = datetime.datetime.now()
                relogio = f"{hora_agora.strftime('%H:%M:%S')}"

                if busca_cep.status_code == 200:
                    localizacao = busca_cep.json()
                    
                    if 'erro' in localizacao:

                        self.rir_do_erro()
                        
                        msg = f"{relogio} Falha: CEP {verificacao} não localizado"
                        self.print_e_escreve(msg, log)
                    
                    else:
                        msg = f"{relogio} Sucesso: CEP {verificacao} é {localizacao['logradouro']}"
                        self.print_e_escreve(msg, log)
                        
                else:
                    msg = f"{relogio} Formato incorreto ou servidor explodiu"
                    self.print_e_escreve(msg, log)