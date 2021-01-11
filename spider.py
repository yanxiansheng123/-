import requests
import os 
from lxml import etree
url=""
header={}
response=requests.get(url,headers=header)
html=response.text
tree=etree.HTML(html)
paiming=tree.xpath()[0]
with open("./1.txt","w",encoding="utf-8") as file:
  file.write(paiming)
print("done")
