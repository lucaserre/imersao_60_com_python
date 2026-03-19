import requests
import datetime
"""
class AuditorDeCeps:

    def print_e_escreve(self, mensagem, dados):
        print(mensagem)
        dados.write(mensagem + '\n')
        
    def __init__(self, ceps):
        self.lista_ceps = ceps


        


    def auditar(self):  

            
            for verificacao in self.lista_ceps:
                print(f'Processando CEP: {verificacao}')
                url = f'https://viacep.com.br/ws/{verificacao}/json/'
                busca_cep = requests.get(url)
                hora_agora = datetime.datetime.now()
                relogio = f"{hora_agora.strftime('%H:%M:%S')}"
                


                if busca_cep.status_code == 200:
                    localizacao = busca_cep.json()
                    
                    if 'erro' in localizacao:
                        AuditorDeCeps(f"{relogio} Falha: CEP {verificacao} não localizado", AuditorDeCeps )
                        
                        

                    else:
                        AuditorDeCeps(f"{relogio} Sucesso: CEP {verificacao} é {localizacao['logradouro']}", AuditorDeCeps)
                        
                else:
                    AuditorDeCeps(f"{relogio} Formato incorreto ou servidor explodiu", AuditorDeCeps)



ceps = ['25725380', '99999-999', '01001-000', '20000-000', '8979797-8000']
meu_robo = AuditorDeCeps(ceps)
meu_robo.auditar()
"""



#Essa foi a versão corrigida pelo Gemini, porque eu estava ficando confuso quanto a utilização das funções dentro da classe. ( O script anterior está incorreto)

class AuditorDeCeps:

    # 1. Adicionei 'self' aqui. Agora o robô sabe que essa ferramenta é dele.
    def print_e_escreve(self, mensagem, arquivo_destino):
        print(mensagem)
        # O arquivo precisa do \n, o print não
        arquivo_destino.write(mensagem + '\n') 
        
    def __init__(self, ceps_recebidos):
        self.lista_ceps = ceps_recebidos

    def auditar(self):
        # Abrimos o arquivo aqui para usar durante todo o processo
        with open('auditoria_robo.txt', 'w', encoding='utf-8') as log:
            
            for verificacao in self.lista_ceps:
                print(f'Processando CEP: {verificacao}')
                
                url = f'https://viacep.com.br/ws/{verificacao}/json/'
                busca_cep = requests.get(url)
                
                hora_agora = datetime.datetime.now()
                relogio = f"{hora_agora.strftime('%H:%M:%S')}"

                if busca_cep.status_code == 200:
                    localizacao = busca_cep.json()
                    
                    if 'erro' in localizacao:
                        msg = f"{relogio} Falha: CEP {verificacao} não localizado"
                        # 2. O PULO DO GATO: self.funcao(...)
                        # "Eu mesmo (self), use a ferramenta de escrever nesse arquivo (log)"
                        self.print_e_escreve(msg, log)
                        
                    else:
                        msg = f"{relogio} Sucesso: CEP {verificacao} é {localizacao['logradouro']}"
                        self.print_e_escreve(msg, log)
                        
                else:
                    msg = f"{relogio} Formato incorreto ou servidor explodiu"
                    self.print_e_escreve(msg, log)

# --- USO DO ROBÔ ---
lista_ceps = ['25725380', '99999-999', '01001-000']

# 1. Fábrica, crie o robô 'jarvis'
jarvis = AuditorDeCeps(lista_ceps)

# 2. Jarvis, trabalhe!
jarvis.auditar()