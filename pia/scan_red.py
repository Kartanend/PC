import nmap
import csv 
import logging


def scaner_red(ip,csvName):
    """
    Escanea la red usando nmap a una IP o rango de ip's.

    Args:
        ip (str): Es la direccion o direcciones ip a escanear. Ejemplos:
            -192.168.0.1 para escanear una sola ip
            -192.168.0.0/24 para escanear un rango de direcciones ip
        
        csvName (str): Es el nombre del archivo con el que se guardará el reporte csv.

    Prints:
        Imprime el estado de cada puerto agrupado por su ip correspondiente.
    
    Generates:
        Genera un archivo csv donde guarda el reporte del escaneo.
    """
    try:
        nmScan = nmap.PortScanner()
        print("Escaneando...")
        scan_range=nmScan.scan(hosts=ip)
        hosts=scan_range['scan']
        csv_file="{}.csv".format(csvName)
        print("Sanitizando...")    


        for ip, ip_info in hosts.items():
            print("\n", ip)
            for port, port_info in ip_info["tcp"].items():
                status = port_info["state"]
                print(f"port {port} is {status}.")

        with open(csv_file, "w", newline="") as csv_archivo:
            escritor = csv.writer(csv_archivo)
            contenido = nmScan.csv().split("\r\n")
            for linea in contenido:
                escritor.writerow(linea.split(";"))
            del escritor
    except:
        logging.error("Error al escanear las ip(s)")
