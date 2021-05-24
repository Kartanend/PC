#Autor: Diego Moreno Villarreal
import json
import requests
import logging

def obtener_Correos(apikey, dominio, limite):
    try:
        url = "https://api.hunter.io/v2/domain-search?domain={dominio}&limit={limite}&api_key={apikey}"
        url =url.format(apikey=apikey, limite=limite, dominio=dominio)
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
