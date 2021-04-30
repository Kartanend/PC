import requests
from bs4 import BeautifulSoup as bs
import argparse
from PIL import Image
from PIL.ExifTags import TAGS
import glob

parser=argparse.ArgumentParser()
parser.add_argument('-link',type=str, required=True)
args=parser.parse_args()

print(args.link)
url=args.link
soup=bs(requests.get(url).content,"html.parser")
img_tags=soup.find_all('img')
urls=[]
for i in img_tags:
    urls.append(i.attrs.get("src"))

uris=[]
for val in urls:
    if val!= None:
        uris.append(val)

j=0
for i in uris:
    with open("{}".format(j),'wb') as f:
        response=requests.get(i)
        f.write(response.content)
        f.close()
        j=j+1

img = Image.open("0")
exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }
print(exif)
