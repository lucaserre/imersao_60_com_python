from collections import Counter
import math
from matplotlib import pyplot as plt
import tkinter as tk
from tkinter import filedialog
import pefile

root = tk.Tk()
root.withdraw()

def calcular_entropia(bloco_de_dados):

        entropia  = 0
        tamanho_bloco = len(bloco_de_dados)
        contagem = Counter(bloco_de_dados)
        
        for byte_atual in contagem:
        
            frequencia_byte = contagem[byte_atual]
            probabilidade = frequencia_byte/tamanho_bloco
            logaritimos = math.log2(probabilidade)
            shannon = probabilidade * logaritimos
            entropia += shannon * -1

        return entropia

def gerar_grafico(dados_entropia, secoes_entropia, cores_entropia):

    
    plt.figure(figsize=(10, 6))
    
    plt.plot(dados_entropia, color=cores_entropia, linewidth=1, label='Entropia do Arquivo')
    plt.axhline(y=7.5, color='red', linestyle='--', linewidth=2, label='Limiar de Suspeita (7.5)')
    plt.fill_between(range(len(dados_entropia)), dados_entropia, color=cores_entropia, alpha=0.3)
    plt.xticks(range(len(dados_entropia)), secoes_entropia, color=cores_entropia)
    plt.ylim(0, 8.5)
    plt.title('Análise de Entropia de Shannon', fontsize=14)
    plt.xlabel('Blocos de Dados (Offset)', fontsize=12)
    plt.ylabel('Entropia (Bits)', fontsize=12)
    plt.legend(loc='lower right')
    plt.show()
    
def analisar_arquivo(caminho_do_arquivo):

    lista_entropia = []
    lista_tamanho_fisico = []
    lista_tamanho_virtual = []
    lista_nomes = []
    lista_importacoes_processos = []
    secoes_comuns = ['.text', '.data', '.rdata', '.rsrc', '.reloc', '.idata', '.bss', '.edata', '.tls', '.pdata', '.debug', '.CRT', '.00cfg']

    pe = pefile.PE(caminho_do_arquivo)
    cor_atual = "#08fcec"

    if hasattr(pe, 'DIRECTORY_ENTRY_IMPORT'):
        for biblioteca in pe.DIRECTORY_ENTRY_IMPORT:
            for funcao in biblioteca.imports:
                if funcao.name:
                    limpeza_funcao = funcao.name.decode('utf-8')
                    lista_importacoes_processos.append(limpeza_funcao)
    
    quantidade_processos = len(lista_importacoes_processos)

    if quantidade_processos < 10 or quantidade_processos > 100:

        print(f'[WARNING] Suspicious number of processes: {quantidade_processos}')
    
    for secao in pe.sections:
        
        dados_da_secao = secao.get_data()
        local_da_secao = secao.Name.decode('utf-8').strip('\x00')
        memoria_fisica_secao = secao.SizeOfRawData 
        memoria_virtual_secao = secao.Misc_VirtualSize
        
        entropia = calcular_entropia(dados_da_secao)
        lista_entropia.append(entropia)
        lista_nomes.append(local_da_secao)
        lista_tamanho_fisico.append(memoria_fisica_secao)
        lista_tamanho_virtual.append(memoria_virtual_secao)
        
        if not local_da_secao in secoes_comuns:
            print(f'[WARNING]: Suspect Section Name: {local_da_secao}')
        
        if entropia > 7.5 and memoria_fisica_secao < memoria_virtual_secao:
            print(f'[WARNING]: Possible packed script in section:  {local_da_secao} F{memoria_fisica_secao} e V{memoria_virtual_secao} ')
        

    return lista_entropia, lista_nomes, cor_atual
        
leitor_de_pastas = filedialog.askopenfilename(title="Qual arquivo deseja analisar?" )
print(leitor_de_pastas)

plt.style.use('dark_background')

if leitor_de_pastas:
        
    dados, nomes, cores = analisar_arquivo(leitor_de_pastas)
    gerar_grafico(dados, nomes, cores)

else:
    print('Nenhum arquivo foi selecionado')


