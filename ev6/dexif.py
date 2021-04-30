import requests
from bs4 import BeautifulSoup as bs
import argparse
from PIL import Image
from PIL.ExifTags import TAGS
import glob
import os

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
dir="./images/"
if not os.path.exists(os.path.dirname(dir)):
    os.makedirs(os.path.dirname(dir))

for i in uris:
    with open("./images/{}".format(j),'wb') as f:
        response=requests.get(i)
        f.write(response.content)
        f.close()
        j=j+1

i=0
while (i<len(uris)):
    cmd="identify -verbose ./images/{0} > ./images/{0}.txt".format(i)
    os.system(cmd)
    i=i+1
