import argparse
import detectSpanish


parser=argparse.ArgumentParser()
parser.add_argument("--modo", help="Modo del programa", action="store")
parser.add_argument("--message",help="Mensaje",action="store")
parser.add_argument("--clave")
args= parser.parse_args()
SYMBOLS="ABCDEFGHIJKLMNOPQRSTUVXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."
translated=''
if args.modo == "cifrar":
    message=args.message
    key=len(args.clave)
    
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex=SYMBOLS.find(symbol)
            translatedIndex=symbolIndex+key

            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex-len(SYMBOLS)
            elif translatedIndex <0:
                translatedIndex = translatedIndex+len(SYMBOLS)

            translated=translated+SYMBOLS[translatedIndex]
        else:
            translated=translated+symbol

    print(translated)
    
elif args.modo == "descifrar":
    message=args.message
    key=len(args.clave)
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex=SYMBOLS.find(symbol)
            translatedIndex=symbolIndex-key
            
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex-len(SYMBOLS)
            elif translatedIndex <0:
                translatedIndex = translatedIndex+len(SYMBOLS)
                
            translated = translated + SYMBOLS[translatedIndex]
        else:
            translated = translated + symbol
    print(translated) 
                   
elif args.modo == "crackear":
    message=args.message
    
    for key in range(len(SYMBOLS)):
        translated=''    
        for symbol in message:
            if symbol in SYMBOLS:
                symbolIndex=SYMBOLS.find(symbol)
                translatedIndex = symbolIndex - key
                
                if translatedIndex <0:
                    translatedIndex=translatedIndex+len(SYMBOLS)
                
                translated = translated + SYMBOLS[translatedIndex]
            else:
                translated=translated+symbol
#        print(translated)                                      
        if (detectSpanish.isSpanish(translated)):
            print("Posible Cadena valida en español")
            response=input("Ingresa la letra D para detener el crackeo-> ")
            if response=='D':
                break

        
