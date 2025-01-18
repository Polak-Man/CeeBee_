import socket
import json

def start_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', port))
    server_socket.listen(1)
    print(f"Serveur en écoute sur le port {port}...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connexion de {addr}")
        data = client_socket.recv(1024).decode('utf-8')
        if data:
            print("Données reçues :", data)
            # Vous pouvez traiter les données ici
            # Par exemple, afficher une image ou une vidéo
        client_socket.close()

if __name__ == "__main__":
    start_server(5000)  # Écoute sur le port 5000