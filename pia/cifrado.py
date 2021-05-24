from time import sleep

def encriptar(mess, key):
    """
    Encripta un mensaje usando cifrado Cesar y luego imprime el mensaje en base a la clave.

    Args:
        mess (str): Es el mensaje a encriptar.

        key (str): Es la llave que dependiendo de su longitud saldra el mensaje cifrado de cierta manera.
    
    Prints:
        Imprime el mensaje encriptado que se obtuvo a partir de la clave.
    """
    print("Procesando cifrado...")
    key = len(key)

    while key >=66:
        key = key-66

    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
    translated = ''

    for symbol in mess:
        # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex + key
            
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]
        else:
            # Append the symbol without encrypting/decrypting:
            translated = translated + symbol

    print("El nuevo mensaje es: ",translated)
