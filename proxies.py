from bs4 import BeautifulSoup
import requests as r

def getProxy():
    website = r.get('https://www.us-proxy.org')
    html = website.text

    soup = BeautifulSoup(html,'html.parser')

    new_soup = soup.tbody

    var = []

    index = 0
    for i in new_soup.find_all('td'):
        var.append(i.text)
#create local lsit
    l = []
    d = {}
    whileIndex = 0
    while(True):
        if (whileIndex < len(var)) and (var[whileIndex+4] == 'elite proxy' or 'anonymous') :
            l.append([var[whileIndex],var[whileIndex+1]])
            d[var[whileIndex]]=var[whileIndex+1]
        else:
            break
        whileIndex += 8
    #return "http://"+str(l[0][0])+":"+str(l[0][1])
    return d
