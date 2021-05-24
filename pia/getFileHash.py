import hashlib
import sys
import logging

def getHash(ruta):
    """
    Obtiene el contenido del archivo recibido por su ruta y luego genera su hash512.

    Args:
        ruta (str): Es la ruta del archivo a generar su codigo hash 512. Esta ruta puede ser
                    relativa o absoluta.

    Prints:
        Imprime el codigo hash 512 del archivo marcado por su ruta.
    """
    h = hashlib.sha512()
    BLOCK_SIZE= 65536
    try:
        with open(ruta,'rb') as f:
            fb = f.read(BLOCK_SIZE)
            while len(fb) > 0:
                h.update(fb)
                fb = f.read(BLOCK_SIZE)
    except IOError:
        logging.error("Archivo no encontrado")
        sys.exit()
    
    
    print(h.hexdigest())        
