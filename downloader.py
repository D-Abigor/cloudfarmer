import requests
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

