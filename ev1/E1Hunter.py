from pyhunter import PyHunter
import csv
import getpass
_author_ = "Daniel Alejandro Cruz Polo"


def busqueda(organizacion):
    resultado = hunter.domain_search(company=organizacion,
                                     emails_type='personal')
    resultado = resultado["emails"]
    return resultado


def guardar_informacion(datos_encontrados):
    keys = datos_encontrados[0].keys()
    with open('test.csv', 'a+', newline='') as out:
        dw = csv.DictWriter(out, keys)
        dw.writeheader()
        dw.writerows(datos_encontrados)


print("Script para buscar información")
apikey = getpass.getpass("Ingresa tu API key: ")
hunter = PyHunter(apikey)
orga = input("Dominio a investigar: ")
datos_encontrados = busqueda(orga)
if datos_encontrados is None:
    exit()
else:
    print(datos_encontrados)
    print(type(datos_encontrados))
    guardar_informacion(datos_encontrados)
