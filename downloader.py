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
    
def download(link,identifier):
    downloadLink = obtainDDL(link)
    response = req.get(downloadLink, stream=True)
    try:
        extension = response.headers["Content-Disposition"].split('.')[-1].strip('"')
    except KeyError:
        extension = "unknown"

    if response.status_code == 200:
        filename = str(identifier) +'.'+ extension
        dirs = os.listdir()
        if filename in dirs:
            print(filename, 'already exists')
            filename = os.path.abspath(str(identifier) + '.' + extension)
            return link,filename
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
        input()
        return
    wait_time = random.uniform(min_delay,max_delay)
    print(f"Waiting {wait_time:.2f} seconds before next download...")
    time.sleep(wait_time)
    filename = os.path.abspath(str(identifier) + '.' + extension)
    return link,filename                                                                            # need to change filename to get full file path
