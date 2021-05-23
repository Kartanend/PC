import argparse
import scan_red
import getFileHash


parser= argparse.ArgumentParser()
parser.add_argument("--task", help="tarea a realizar")
parser.add_argument("--ip", 
                    help="dirección ip en formato CIDR para la tarea de "
                    "escaneo\nEj: 192.168.1.1/24")
parser.add_argument("--csvFile",
                    help="nombre de archivo csv para resultados de scaner de"
                    "red")                   
args = parser.parse_args()

try:
    task = 0
    if args.task == None:
        print("Elige la tarea a realizar")
        print("1.-Escaneo de puertos de toda una red"
              "\n2.-Obtener hash de archivo")
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
            
        ip=args.ip
        csvName=args.csvFile    
        scan_red.scaner_red(ip,csvName)
    
    if args.task == "obtener-hash-archivo" or task ==2:
        getFileHash.getHash()
           
except KeyboardInterrupt:
    exit()              
