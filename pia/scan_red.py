import nmap
import csv 
import logging


def scaner_red(ip,csvName):
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
