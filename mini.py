import requests as r
import os
from urllib.request import urlretrieve
from bs4 import BeautifulSoup

# Holds the download Links
pdfLinks = []


def getLinks(website, Folder_name):
    html = r.get(website)
    readable = html.text

    soup = BeautifulSoup(readable, 'html.parser')

    for links in soup.find_all('a'):
        if links.get('rel') == ['nofollow']:
            pdfLinks.append(links.get('href'))
    # to download the links
    downloadFiles(pdfLinks, Folder_name)


def downloadFiles(downloadLinks, Folder_name):
    index = 0
    #Create Directory Call
    create_project_dir(Folder_name)

    for eachlink in downloadLinks:

        print("Downloading " + eachlink)

        local_filename = Folder_name+"/File" + str(index) + ".pdf"

        try:
            req = r.get(eachlink)
            file = open(local_filename, 'wb')
            for chunk in req.iter_content(1024):
                file.write(chunk)
            file.close()

            print("Downloaded " + str(index + 1) + " File")
        except:
            print("")
            continue
        index += 1
    print("\n Download Complete")


# Each website is a separate project (folder)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating directory ' + directory)
        os.makedirs(directory)

# running the program
getLinks('http://www.engpaper.com/iot-2016.htm', "IOT")
