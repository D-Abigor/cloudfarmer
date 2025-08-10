import requests as req
import os



def obtainHost(link):               # function to find where the files are hosted
    if "google.com" in link:
        host = "google"
    #logic for other providers to be added
    return host

def obtainDDL(link):
    host = obtainHost(link)
    if host == "google":
        fileId = link.split("id")[-1]
        downloadLink = "https://drive.google.com/uc?export=download&id=" + fileId
    else:
        print('unsupported host')
    return downloadLink
    
def download(link,identifier):
    downloadLink = obtainDDL(link)
    response = req.get(downloadLink, stream=True)
    try:
        extension = response.headers["Content-Disposition"].split('.')[-1]
    except KeyError:
        extension = "unknown"

    if response.status_code == 200:
        filename = identifier+'.'+extension
        with open(filename, "wb") as file:
            for chunks in response.iter_content(8192):
                if chunks:
                    try:
                        file.write(chunks)
                    except OSError:
                        print("could not write to drive")
    else:
        print("file could not be downloaded")
        input()
        return
    return link,filename
