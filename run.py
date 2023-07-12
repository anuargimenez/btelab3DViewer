import threading
import webbrowser
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import os


class MyHttpRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=".", **kwargs)


def start_server():
    PORT = 8000  # Cambiar el puerto si es necesario

    # Crear el servidor HTTP
    handler = MyHttpRequestHandler
    with TCPServer(("", PORT), handler) as httpd:
        print("Servidor iniciado en el puerto", PORT)

        # Esperar hasta que se cierre la ventana del navegador
        httpd.serve_forever()


def main():
    # Obtener la URL del servidor HTTP
    server_url = 'http://localhost:8000'  # Cambiar el puerto si es necesario

    # Abrir la URL en una nueva ventana del navegador
    webbrowser.open(server_url, new=2)

    # Iniciar el servidor HTTP en un subproceso
    server_thread = threading.Thread(target=start_server)
    server_thread.start()

    # Esperar hasta que se cierre el subproceso del servidor
    server_thread.join()


if __name__ == "__main__":
    main()
