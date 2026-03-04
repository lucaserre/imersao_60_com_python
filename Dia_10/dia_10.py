import time
import random

lista_clientes = ['Isadora', 'Helen', 'Lucas']

for envio_msg in lista_clientes:
    print (f'Enviando mensagem para {envio_msg}')
    delay = random.randint(1, 5)
    time.sleep(delay)
   
    print(f'Mensagem enviada com sucesso, com delay de {delay} segundos! ')
