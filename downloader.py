import requests
import os
import time
import random


min_delay = 2
max_delay = 5

req = requests.Session()

def obtainHost(link):               # function to find where the files are hosted
    if "google.com" in link:
        host = "google"
    #logic for other providers to be added
    return host

def obtainDDL(link):
    host = obtainHost(link)
    if host == "google":
        fileId = link.split("id")[-1]
        downloadLink = "https://drive.usercontent.google.com/u/0/uc?id" + fileId + "&export=download"
    else:
        print('unsupported host')
    return downloadLink
    
def download(link,identifier,min,max):
    #checking if the file has already been downloaded
    file = [file for file in os.listdir() if file.startswith(str(identifier)+".")]
    if file:
        print(file[0], "already downloaded")
        return link,file[0]

    downloadLink = obtainDDL(link)
    response = req.get(downloadLink, stream=True)
    try:
        extension = response.headers["Content-Disposition"].split('.')[-1].strip('"')
    except KeyError:
        extension = "unknown"


    if response.status_code == 200:
        filename = str(identifier) +'.'+ extension
        with open(filename, "wb") as file:
            for chunks in response.iter_content(8192):
                if chunks:
                    try:
                        file.write(chunks)
                    except OSError:
                        print("could not write to drive")
    else:
        print("file could not be downloaded")
        print(response)
        print(downloadLink)
        filename = str(identifier) +'.'+ 'err'
    wait_time = random.uniform(min,max)
    print(f"Waiting {wait_time:.2f} seconds before next download...")
    time.sleep(wait_time)
    filename = os.path.abspath(str(identifier) + '.' + extension)
    return link,filename                                                                           
