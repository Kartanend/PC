import hashlib
import sys

def getHash():
    print("Ingresa ruta de archivo: ")
    ruta=input()
    h = hashlib.sha256()
    BLOCK_SIZE= 65536
    try:
        with open(ruta,'rb') as f:
            fb = f.read(BLOCK_SIZE)
            while len(fb) > 0:
                h.update(fb)
                fb = f.read(BLOCK_SIZE)
    except IOError:
        print("Archivo no encontrado")
        sys.exit()
    
    
    print(h.hexdigest())        
