import requests
import datetime


"""

class AuditorDeCeps:

    def __init__(self, ceps_recebidos):
        self.lista_localizacao = ceps_recebidos
        
        

    def print_e_escreve(self, mensagem, arquivo_destino):
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
                        msg = f"{relogio} Falha: CEP {verificacao} não localizado" + '\n'

                        self.rir_do_erro()
                        
                    else:
                        msg = f"{relogio} Sucesso: CEP {verificacao} é {localizacao['logradouro']}" + '\n'
                        self.print_e_escreve(msg, log)
                        
                else:
                    msg = f"{relogio} Formato incorreto ou servidor explodiu" + '\n'
                    self.print_e_escreve(msg, log)


    def rir_do_erro(self):
        pass




class AuditorDebochado(AuditorDeCeps):

    def __init__(self, ceps_recebidos):
        super().__init__(ceps_recebidos)
        

    def print_e_escreve(self, mensagem, arquivo_destino):

        print(f'---RELATÓRIO DO ESTAGIÁRIO---' + '\n')
        print(mensagem)
        
        arquivo_destino.write(mensagem + '\n')     
    
    def rir_do_erro(self):
            
        
            print('HAHAHA CEP ERRADO!' + '\n')
    


lista_ceps = ['25725380', '99999-999', '01001-000']
jarvis = AuditorDebochado(lista_ceps)

jarvis.auditar()

"""

# A seguir tem a versão corrigida do meu script, de maneira mais limpa e com comentários

import requests
import datetime

# --- CLASSE PAI (O Robô Sério e Funcional) ---
class AuditorDeCeps:

    def __init__(self, ceps_recebidos):
        # O Pai guarda a lista.
        self.lista_localizacao = ceps_recebidos

    # O método 'normal' de escrever. O Pai sabe fazer isso.
    def print_e_escreve(self, mensagem, arquivo_destino):
        print(mensagem)
        arquivo_destino.write(mensagem + '\n')

    # Um "gancho". O Pai não ri, então aqui é vazio (pass).
    # Mas ele deixa o espaço para o filho rir se quiser.
    def rir_do_erro(self):
        pass 

    def auditar(self):
        with open('auditoria_robo.txt', 'w', encoding='utf-8') as log:
            
            # O 'self.lista_localizacao' funciona no filho 
            # porque ele herdou tudo do pai!
            for verificacao in self.lista_localizacao:
                print(f'Processando CEP: {verificacao}')
                
                url = f'https://viacep.com.br/ws/{verificacao}/json/'
                busca_cep = requests.get(url)
                
                hora_agora = datetime.datetime.now()
                relogio = f"{hora_agora.strftime('%H:%M:%S')}"

                if busca_cep.status_code == 200:
                    localizacao = busca_cep.json()
                    
                    if 'erro' in localizacao:
                        # O Pai chama o método de rir. 
                        # Se for o Pai, não acontece nada (pass).
                        # Se for o Filho, ele ri (HAHAHA).
                        self.rir_do_erro()
                        
                        msg = f"{relogio} Falha: CEP {verificacao} não localizado"
                        self.print_e_escreve(msg, log)
                    
                    else:
                        msg = f"{relogio} Sucesso: CEP {verificacao} é {localizacao['logradouro']}"
                        self.print_e_escreve(msg, log)
                        
                else:
                    msg = f"{relogio} Formato incorreto ou servidor explodiu"
                    self.print_e_escreve(msg, log)


# --- CLASSE FILHO (O Robô Debochado) ---
class AuditorDebochado(AuditorDeCeps):

    # NOTA: Eu APAGUEI o __init__ daqui.
    # O Python vai usar o __init__ do Pai automaticamente.
    # A lista vai ser guardada no self.lista_localizacao do mesmo jeito.

    # AQUI ESTÁ A MÁGICA (Sobrescrita / Override)
    # O filho muda como o 'print_e_escreve' funciona.
    def print_e_escreve(self, mensagem, arquivo_destino):
        # 1. Faz a graça do estagiário
        cabecalho = "--- RELATÓRIO DO ESTAGIÁRIO ---"
        print(cabecalho)
        arquivo_destino.write(cabecalho + '\n')
        
        # 2. Chama o pai para fazer o trabalho braçal (escrever a mensagem real)
        # Assim você não precisa reescrever o comando .write de novo!
        super().print_e_escreve(mensagem, arquivo_destino)

    # O filho preenche o "gancho" que o pai deixou vazio
    def rir_do_erro(self):
        print('HAHAHA CEP ERRADO!')

# --- TESTANDO ---

lista_ceps = ['25725380', '99999-999', '01001-000']

print(">>> ROBÔ DEBOCHADO TRABALHANDO:")
jarvis = AuditorDebochado(lista_ceps)
jarvis.auditar()

# Se você quiser testar o Pai sério, agora ele funciona também:
# print("\n>>> ROBÔ SÉRIO TRABALHANDO:")
# robo_serio = AuditorDeCeps(lista_ceps)
# robo_serio.auditar()