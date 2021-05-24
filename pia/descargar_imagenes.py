# Codigo adaptado por: Diego Moreno Villarreal
# Fernando Rafael Hernandez Rodriguez
# Autor original:  castro-miguel-1993
# Github: https://github.com/castro-miguel-1993/pyfiles


import urllib.request
from urllib.request import urlopen, Request
import os
import requests
from bs4 import BeautifulSoup
import logging

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
i = 0
def download(url,folder):
	global i
	with requests.get(url, stream=True) as r:
		r.raise_for_status()
		if "?" in url:
			url = url.split("?")[-2]
		try:
			with open(folder+'/'+str(i)+url.split('/')[-1], 'wb') as f:
				for chunk in r.iter_content(chunk_size=8192): 
					f.write(chunk)
				i=i+1
		except Exception as e:
			print(e)

def download_img(url_descarga, directory):
    try:
        if not os.path.exists(directory):
            os.mkdir(directory)

        req = Request(url=url_descarga, headers=headers)
        datos = urllib.request.urlopen(req).read().decode()
        soup = BeautifulSoup(datos,features="html.parser")
        
        # to images
        tags = soup('img')
        for tag in tags:
            url = tag.get('src')
            if not 'data:' in url:
                if 'http' in url:
                    download(url,directory)
                else:
                    if url[0]=="/":
                        split_url = url_descarga.split('/')
                        url = split_url[0]+"//"+split_url[2]+url 
                    else:
                        url = url_descarga+"/"+url 
                    download(url,directory)
			
        print("Imagenes descargadas correctamente")
    except Exception as e:
        logging.error(e)
