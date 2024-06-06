import socket
import ipaddress
import math
import errno


def gerar_ips(inicio, fim):
    primeiro_ip = ipaddress.ip_address(inicio)
    ultimo_ip = ipaddress.ip_address(fim)
    lista_ips = []
    
    for net in ipaddress.summarize_address_range(primeiro_ip, ultimo_ip):
        for ip in net:
            lista_ips.append(str(ip))
    
    return lista_ips
print("Informe os Hosts a serem escaneados")
primeiro_ip = input("Primeiro IP\n")
ultimo_ip = input("Ultimo IP\n")
ips = gerar_ips(primeiro_ip, ultimo_ip)

portas = [22, 80, 443, 8080, 8443]
for ip in ips:
    print(f"\nVerificando host: {ip}")
    for porta in portas:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1) 
        result = s.connect_ex((ip, porta))
        
        if result == 0:
            print(f"Porta {porta} [ABERTA]\n")
        else:
            print(f"Porta {porta} [FECHADA]\n")
        
        s.close()
