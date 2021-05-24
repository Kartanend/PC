import hashlib
import sys
import logging

def getHash():
    print("Ingresa ruta de archivo: ")
    ruta=input()
    h = hashlib.sha512()
    BLOCK_SIZE= 65536
    try:
        with open(ruta,'rb') as f:
            fb = f.read(BLOCK_SIZE)
            while len(fb) > 0:
                h.update(fb)
                fb = f.read(BLOCK_SIZE)
    except IOError:
        logging.error()("Archivo no encontrado")
        sys.exit()
    
    
    print(h.hexdigest())        
