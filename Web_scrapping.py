
import re
import requests
from bs4 import BeautifulSoup

url="https://en.wikipedia.org/wiki/List_of_songs_recorded_by_Arijit_Singh"
req=requests.get(url)
soup=BeautifulSoup(req.text,'lxml')
#print(soup)
string=[]
f=""
title = soup.findAll('tr')
file= open("C:\\Users\Asus\Desktop\\py files\\song.txt","w",errors="ignore")
file= open("C:\\Users\Asus\Desktop\\py files\\song.txt","w",encoding="UTF-8")
for t in title:
    #print(t)
    comp = str(t)
    file.write(comp)
file = open("C:\\Users\Asus\Desktop\\py files\\song.txt", "r")
for r in file.readlines():
    if r.startswith("<th"):
        ty = r.strip()
        f = re.findall("<i><a.+>(.+)</a></i>", ty)
        string.append(f)
    if r.startswith("<td"):
        ty = r.strip()
        f1 = re.findall("<td>(.+)", ty)
        string.append(f1)
print(string)

