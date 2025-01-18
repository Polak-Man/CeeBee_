import socket
import json
import tkinter as tk
from tkinter import scrolledtext

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
            # Afficher les données dans la fenêtre Tkinter
            display_data(data)
        client_socket.close()

def display_data(data):
    # Créer une nouvelle fenêtre Tkinter
    window = tk.Tk()
    window.title("Données reçues")

    # Créer un widget Text pour afficher les données
    text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=50, height=20)
    text_area.pack(padx=10, pady=10)

    # Insérer les données dans le widget Text
    text_area.insert(tk.END, data)

    # Bouton pour fermer la fenêtre
    close_button = tk.Button(window, text="Fermer", command=window.destroy)
    close_button.pack(pady=5)

    # Lancer la boucle principale de Tkinter
    window.mainloop()

if __name__ == "__main__":
    start_server(5000)  # Écoute sur le port 5000