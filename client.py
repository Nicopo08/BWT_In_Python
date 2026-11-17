import BWT
import socket as sck

messaggio=input("inserisci una parola ")

with sck.socket(sck.AF_INET, sck.SOCK_STREAM) as client:
    client.connect(("127.0.0.1", 5000))
    print ("Connessione al server stabilita")

    client.sendall(messaggio.encode())
    print("Messaggio inviato al sevrer")

    risposta=client.recv(1024)

    print("Risposta del server: ", risposta.decode())

print("Client terminato")