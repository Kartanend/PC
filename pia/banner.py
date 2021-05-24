import socket
import logging

def obtener_banner(ip):
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
