import argparse
import scan_red
import getFileHash
import cifrado
import correos
import getpass
import subprocess
import logging
from hunter import obtener_Correos
from descargar_imagenes import download_img
from banner import obtener_banner


if __name__ == "__main__":
    parser= argparse.ArgumentParser()
    parser.add_argument("--task", help="tarea a realizar: 1.- [escaneo-de-puertos] Escaneo de puertos de una IP, un rango de IP's o toda una red"
                "\n2.- [obtener-hash-archivo] Obtener hash de archivo"
                "\n3.- [cifrar-mensaje] cifrar-mensaje"
                "\n4.- [enviar-correo] enviar-correo. -->[IMPORTANTE]Solo texto, solo GMAIL"
                "\n5.- [obtener-procesos] Imprime los procesos del sistema y los guarda en un archivo txt"
                "\n6.- [obtener-correos] Obtiene correos publicos de un dominio"
                "\n7.- [descargar-imagenes] Descarga imagenes de una pagina web si es posible"
                "\n8.- [obtener-banner] Trata de obtener el banner de algun servidor web.",
                choices=["escaneo-de-puertos", "obtener-hash-archivo", "cifrar-mensaje", "enviar-correo",
                         "obtener-procesos", "obtener-correos", "descargar-imagenes", "obtener-banner"])
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
    parser.add_argument('--para', dest='para', help='Quien envia')
    parser.add_argument('--asunto', dest='asunto', help='Quien envia')
    parser.add_argument('--cuerpo', dest='cuerpo', help='Quien envia')
    parser.add_argument('--txt', dest='txt', help='Nombre del archivo txt donde se guardan los procesos o correos. '
                        "Se guarda por defecto en un archivo llamado \"archivo.txt\"",
                        default="archivo")
    parser.add_argument('--limite', dest='limite', help="Limite de correos pedidos hacia la API hunter",
                        default=10, type=int)
    parser.add_argument('--apikey', dest='apikey', help="API key para la api de hunter")
    parser.add_argument('--dominio', dest='dominio', help="Dominio a buscar correos")
    parser.add_argument('--url', dest='url', help="URL a descargar imagenes con web scrapping o para obtener el banner del servidor")

    args = parser.parse_args()

    try:
        task = 0
        if args.task == None:
            print("Elige la tarea a realizar")
            print("1.-Escaneo de puertos de toda una red"
                "\n2.-Obtener hash de archivo"
                "\n3.-Cifrar un mensaje"
                "\n4.-Enviar un correo"
                "\n5.-Obtener procesos del sistema"
                "\n6.-Obtener correos de un dominio"
                "\n7.-Descargar imagenes de una pagina web"
                "\n8.-Obtener el banner de un servidor web")
            task=int(input("Opcion seleccionada-> "))

        if args.task == "escaneo-de-puertos" or task == 1:
            ip = args.ip
            csvName = args.csvFile

            if ip == None:
                ip = input("Ingresa IP donde empezará el escaneo en formato CIDR: ")
            
            if csvName == None:
                csvName = input("Ingresa Nombre de archivo csv para el registro: ")
            
            scan_red.scaner_red(ip,csvName)
        
        elif args.task == "obtener-hash-archivo" or task == 2:
            getFileHash.getHash()

        elif args.task == "cifrar-mensaje" or task == 3:
            message = args.mess
            key = args.key

            if message == None:
                message = input("Ingresa el mensaje a cifrar: ")

            if key == None:
                key = input("Necesito una clave: ")

            cifrado.encriptar(message,key)

        elif args.task == "enviar-correo" or task == 4:
            usuario = args.usuario
            para = args.para
            asunto = args.asunto
            cuerpo = args.cuerpo

            if usuario == None:
                usuario = input("Ingresa tu correo: ")

            print("Ingresa tu contreaseña: ")
            pwd = getpass.getpass()
                
            if para == None:
                para =input("Correo destino: ")

            if asunto == None:
                asunto = input("Ausnto: ")

            if cuerpo == None:
                cuerpo = input("Escribe tu mensaje: ")
                
            correos.env_correo(usuario,pwd,para,asunto,cuerpo)
                
        elif args.task == "obtener-procesos" or task == 5:
            comando = "powershell -ExecutionPolicy ByPass -File procesos.ps1"
            tabla = subprocess.run(comando, stdout=subprocess.PIPE)
            print(tabla.stdout.decode())

            with open(args.txt+".txt" , "wb") as txt:
                txt.write(tabla.stdout)

        elif args.task == "obtener-correos" or task == 6:
            key = args.apikey
            dominio = args.dominio

            if key == None:
                key = input("Ingrese su API key de hunter: ")

            if dominio == None:
                dominio = input("Ingrese el dominio de correos a buscar: ")

            correos = obtener_Correos(key, dominio, args.limite)

            with open(args.txt+".txt", "w") as txt:
                txt.write("Dominio: "+dominio+"\n")
                for correo in correos:
                    txt.write(correo+"\n")
                

        elif args.task == "descargar-imagenes" or task == 7:
            url = args.url
            if url == None:
                url = input("Ingrese una URL para descargar las imagenes: ")

            download_img(url, "imagenes")

        elif args.task == "obtener-banner" or task == 8:
            url = args.url
            if url == None:
                url = input("Ingrese una url para tratar de obtener su banner: ")
            
            obtener_banner(url)

        else:
            print("Opcion no valida, terminando programa...")
    
    except KeyboardInterrupt:
        exit()              
    except Exception as e:
        logging.error("Exception error")