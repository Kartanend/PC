import nmap
import csv 

def scaner_red(ip,csvName):
    nmScan = nmap.PortScanner()
    print("escaneando")
    scan_range=nmScan.scan(hosts=ip)
    hosts=scan_range['scan']
    csv_file="{}.csv".format(csvName)
    print("sanitizando")    
    csv_columns=[]
    valid_hosts=hosts.copy()
    for ip in hosts.keys():
        if "tcp" in hosts[ip]:
            #para fines de la tarea eliminé mis direcciones mac
            del hosts[ip]['addresses']['mac']        
           #print(hosts[ip],"\n")
        else:
            del valid_hosts[ip]


    csv_columns=valid_hosts.keys()

    print("Escribiendo csv...espere")

    with open(csv_file,"w") as f:
        for key in valid_hosts.keys():
            f.write("/%s, %s\n"%(key, valid_hosts[key])) 
