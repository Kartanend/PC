import socket
import logging

def obtener_banner(ip):
    """
    Trata de obtener el banner de un servidor web para descrubrir tecnologia
    que usa y encotrar vulnerabilidades. Solo trabaja sobre el puerto 80.

    Args:
        ip (str): Es la dirección ip del servidor, el cual también puede ser 
                  su nombre de dominio. Ejemplo:
                    - 18.5.1.0
                    - www.google.com
    
    Prints:
        Imprime la respuesta del servidor en HTML.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, 80))

        http_get = "GET / HTTP/1.1\nHost"+ip+"\n\n"
        http_get = http_get.encode()
        data=""
   
        sock.sendall(http_get)
        data=sock.recvfrom(1024)
        print (data[0].decode())
    except socket.error:
        logging.error("Socket error")
    finally:
        print("Closing connection")
        sock.close()
