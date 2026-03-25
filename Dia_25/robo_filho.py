from robo_base import AuditorDeCeps

class AuditorDebochado(AuditorDeCeps):


    def print_e_escreve(self, mensagem, arquivo_destino):
        
        cabecalho = "--- RELATÓRIO DO ESTAGIÁRIO ---"
        print(cabecalho)
        arquivo_destino.write(cabecalho + '\n')
        

        super().print_e_escreve(mensagem, arquivo_destino)

    
    def rir_do_erro(self):
        print('HAHAHA CEP ERRADO!')
