import argparse
import scan_red
import getFileHash
import cifrado
import correos
import getpass
parser= argparse.ArgumentParser()
parser.add_argument("--task", help="tarea a realizar: 1.- Escaneo de puertos de toda una red"
              "\n2.- Obtener hash de archivo"
              "\n3.- cifrar-mensaje"
              "\n4.- enviar-correo. -->[IMPORTANTE]Solo texto, solo GMAIL")
parser.add_argument("--ip", 
                    help="dirección ip en formato CIDR para la tarea de "
                    "escaneo\nEj: 192.168.1.1/24")
parser.add_argument("--csvFile",
                    help="nombre de archivo csv para resultados de scaner de"
                    "red")
#ARGUMENTOS PARA EL CIFRADO
parser.add_argument('--mensaje', dest='mess', help='mensaje a esconder')
parser.add_argument('--clave', dest='key', help='argumento necesario para cifrar')

#AERGUMENTOS PARA EL ENVIO DE CORREOS
parser.add_argument('--usuario', dest='usuario', help='Quien envia')
#parser.add_argument('--contraseña', dest='user', help='contraseña de ')
parser.add_argument('--para', dest='para', help='Quien envia')
parser.add_argument('--asunto', dest='asunto', help='Quien envia')
parser.add_argument('--cuerpo', dest='cuerpo', help='Quien envia')

args = parser.parse_args()

try:
    task = 0
    if args.task == None:
        print("Elige la tarea a realizar")
        print("1.-Escaneo de puertos de toda una red"
              "\n2.-Obtener hash de archivo"
              "\n3.-Cifrar un mensaje"
              "\n4.-Enviar un correo")
        task=int(input("Opcion seleccionada-> "))

    if args.task == "escaneo-de-puertos" or task == 1:
        if args.ip == None and args.csvFile == None:
            print("Ingresa IP donde empezará el escaneo en formato CIDR: ")
            ip=input()
            print("Ingresa Nombre de archivo csv para el registro: ")
            csvName=input()

        elif args.ip != None or args.csvFile == None:
            print("Ingresa Nombre de archivo csv para el registro: ")
            csvName=input()
            ip=args.ip
        elif args.ip == None or args.csvFile != None:
            print("Ingresa IP donde empezará el escaneo en formato CIDR: ")
            ip=input()            
            csvName=args.csvFile
        else:    
            ip=args.ip
            csvName=args.csvFile
            
        scan_red.scaner_red(ip,csvName)
    
    if args.task == "obtener-hash-archivo" or task == 2:
        getFileHash.getHash()

    if args.task == "cifrar-mensaje" or task == 3:
        if args.mess == None and args.key == None:
            print("Ingresa el mensaje a cifrar: ")
            message=input()
            print("Necesito una clave: ")
            key=input()

        elif args.mess != None and args.key != None:
            message=args.mess
            key=args.key

        elif args.mess != None or args.key == None:
            print("Necesito una clave: ")
            key=input()
            message=args.mess
        elif args.mess == None or args.key != None:
            print("Ingresa el mensaje a cifrar: ")
            message=input()            
            key=args.key
        else:    
            message=args.mess
            key=args.key
            
        cifrado.encriptar(message,key)

    if args.task == "enviar-correo" or task == 4:
        if args.usuario == None and args.para == None and args.asunto == None and args.cuerpo == None:
            usuario = input("Ingresa tu correo: ")
            print("Ingresa tu contreaseña: ")
            pwd = getpass.getpass()
            para =input("Para: ")
            asunto = input("Ausnto: ")
            cuerpo = input("Escribe tu mensaje: ")
        elif args.usuario != None and args.para == None and args.asunto == None and args.cuerpo == None:
            usuario = args.usuario
            print("Ingresa tu contreaseña: ")
            pwd = getpass.getpass()
            para =input("Para: ")
            asunto = input("Ausnto: ")
            cuerpo = input("Escribe tu mensaje: ")
        elif args.usuario == None and args.para != None and args.asunto == None and  args.cuerpo == None:
            usuario = input("Ingresa tu correo: ")
            print("Ingresa tu contreaseña: ")
            pwd = getpass.getpass()
            para = args.para
            asunto = input("Ausnto: ")
            cuerpo = input("Escribe tu mensaje: ")
        elif args.usuario == None and args.para == None and args.asunto != None and args.cuerpo == None:
            usuario = input("Ingresa tu correo: ")
            print("Ingresa tu contreaseña: ")
            pwd = getpass.getpass()
            para =input("Para: ")
            asunto = args.asunto
            cuerpo = input("Escribe tu mensaje: ")
        elif args.usuario == None and args.para == None and args.asunto == None and args.cuerpo != None:
            usuario = input("Ingresa tu correo: ")
            print("Ingresa tu contreaseña: ")
            pwd = getpass.getpass()
            para =input("Para: ")
            asunto = input("Ausnto: ")
            cuerpo = args.cuerpo
        else:
            usuario = args.usuario
            para = args.para
            asunto = args.asunto
            cuerpo = args.cuerpo
            print("Ingresa tu contreaseña: ")
            pwd = getpass.getpass()
            
        correos.env_correo(usuario,pwd,para,asunto,cuerpo)
            
except KeyboardInterrupt:
    exit()              
