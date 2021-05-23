#import argparse
#import detectSpanish
from time import sleep
#parser = argparse.ArgumentParser()
#parser.add_argument('-tarea', dest='task', help='cif.- cifra el mensaje \n'+
#                   'des.-descifra el mensaje\n crk.- crackea el mensaje')
#parser.add_argument('-mensaje', dest='mess', help='mensaje a esconder')
#parser.add_argument('-clave', dest='key', help='argumento necesario para cifrar')

#params = parser.parse_args()
#print(params.task)
#print(params.mess)
#print(params.key)
def encriptar(mess, key):
    espacios = 1
    while espacios > 0:
        espacios = key.count(' ')
        if key.isalpha() == False:
            espacios += 1
    key = len(key)

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

    print("Procesando cifrado...")
    sleep(3)
    print("El nuevo mensaje es: ",translated)

"""def desencriptar(menss, key):
    espacios = 1
    while espacios > 0:
        espacios = key.count(' ')
        if key.isalpha() == False:
            espacios += 1
    key = len(key)

    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

    translated = ''

    for symbol in mess:
        # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key
            
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]
        else:
            # Append the symbol without encrypting/decrypting:
            translated = translated + symbol

    print("procesando descifrado...")
    sleep(3)
    print("Texto claro: ",translated)"""

"""def crack(mess):
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

    # Loop through every possible key:
    for key in range(len(SYMBOLS)):
        # It is important to set translated to the blank string so that the
        # previous iteration's value for translated is cleared.
        translated = ''

        # The rest of the program is almost the same as the original program:

        # Loop through each symbol in `message`:
        for symbol in mess:
            if symbol in SYMBOLS:
                symbolIndex = SYMBOLS.find(symbol)
                translatedIndex = symbolIndex - key

                # Handle the wrap-around:
                if translatedIndex < 0:
                    translatedIndex = translatedIndex + len(SYMBOLS)

                # Append the decrypted symbol:
                translated = translated + SYMBOLS[translatedIndex]

            else:
                # Append the symbol without encrypting/decrypting:
                translated = translated + symbol
                #translated = translated.upper()

        # Display every possible decryption: ------quita el import de spanish, 
        print('Key #%s: %s' % (key, translated))
        if (detectSpanish.isSpanish(translated)):
            print("posible ESPAÑOL -^")"""
             
        
#def main():
#    if params.task == "cif" :
 #       encriptar(params.mess, params.key)

 #   elif params.task == "des" :
  #      desencriptar(params.mess, params.key)

   # elif params.task == "crk" :
    #    crack(params.mess)

    #else:
     #   print("[ERROR].- opcion invalida")

#if __name__ =="__main__":
 #   main()
