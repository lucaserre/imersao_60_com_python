ip_ruins = ['10.0.0.1', '192.168.1.50', '172.16.0.10']

with open('blacklist.txt', 'w') as arquivo:
    for ip in ip_ruins:
        arquivo.write(f"{ip}\n") 
        
        print(f"Bloqueado: {ip}")