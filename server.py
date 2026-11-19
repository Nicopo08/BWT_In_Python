from BWT import trasformazione
import socket as sck

with sck.socket(sck.AF_INET, sck.SOCK_STREAM) as server:

    IP="127.0.0.1"
    PORTA=5000

    server.bind((IP, PORTA))
    server.listen()

    print ("Server in ascolto su ", IP, " e porta ", PORTA)

    connessione, indirizzo_client = server.accept()

    with connessione:

        print("Socket di connessione: ", connessione.getsockname())

        dati= connessione.recv(1024)
        parola=dati.decode()
        messaggio_finale=trasformazione(parola)
        
        connessione.sendall(messaggio_finale.encode())


print("Server terminato")

