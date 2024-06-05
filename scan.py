import socket
import ipaddress

def gerar_ips(inicio, fim):
    inicio_ip = ipaddress.ip_address(inicio)
    fim_ip = ipaddress.ip_address(fim)
    ip_list = []
    
    for net in ipaddress.summarize_address_range(inicio_ip, fim_ip):
        for ip in net:
            ip_list.append(str(ip))
    
    return ip_list

inicio_ip = input("Primeiro IP\n")
fim_ip = input("Ultimo IP\n")
ips = gerar_ips(inicio_ip, fim_ip)

portas = [22, 80, 443, 8080, 8443]
for ip in ips:
    print(f"\nVerificando.. {ip}")
    for porta in portas:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1) 
        result = s.connect_ex((ip, porta))
        
        if result == 0:
            print(f"Porta {porta} [ABERTA]\n")
        else:
            print(f"Porta {porta} [FECHADA]\n")
        
        s.close()
