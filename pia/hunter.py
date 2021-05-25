#Autor: Diego Moreno Villarreal
import json
import requests
import logging

def obtener_Correos(apikey, dominio, limite):
    """
    Realiza una peticion a la API de hunter para obtener correos publicos del dominio indicado.

    Args:
        apikey (str): Es la api key necesaria para poder realizar la petición a la API.
        dominio (str): Es el dominio de correos a buscar. Por ejemplo:
                       - uanl.edu.mx
        limite (int): Es el limite para la cantidad de correos a recibir como maximo.
    
    Returns:
        Regresa una lista de correos recibidos. Por ejemplo:
        [
            "correo1@uanl.edu.mx", "correo2@uanl.edu.mx"
        ]
    """
    try:
        url = "https://api.hunter.io/v2/domain-search?domain={dominio}&limit={limite}&api_key={apikey}"
        url =url.format(apikey=apikey, limite=limite, dominio=dominio)
        #print(url)
        page = requests.get (url)
        print ("La respuesta HTTP:", page.status_code)
        if page.status_code == 200:
            hunter = json.loads(page.content)

            correos = list()
            for datos in hunter["data"]["emails"]:
                print(datos["value"])
                correos.append(datos["value"])
                
            return correos
        else:
            raise "Ocurrió un error inesperado"
    except Exception as e:
        logging.error(e)
