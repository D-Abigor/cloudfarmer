import csv_handler as csvm
import downloader as dwn
import csv


print("before starting please ensure your column containing the links has the heading renamed to 'link/links'")
input()

linkmaps,inputFileName= csvm.processcsv()               # linkmaps --> 

originalCsv = []
linkFile = {}                                           # dictionary with key value pair --> links:filename

with open(inputFileName, "r") as original:
    reader = csv.reader(original)
    for rows in reader:
        originalCsv.append(rows)

for columns in range(len(originalCsv[0])):
    if originalCsv[0][columns] in "links":
        linkIndex = columns

import os
folder = "cloudfarmer downloads"
try:
    os.mkdir(folder)
except FileExistsError:
    pass
except OSError as error:
    print(f"unable to generate '{folder}': {error}")
    input()
try:
    os.chdir("cloudfarmer downloads")
except FileNotFoundError:
    print(f"Fatal: '{folder}' not found.")
except OSError as error:
    print(f"Fatal: Unable to access '{folder}': {e}")

print("folders to store downloads were successfuly created/accessed")


# iterating through all the linkmaps [ui:links] to download files and update linkFile [link:filename]
for identifiers in linkmaps:
    link,filename = dwn.download(linkmaps[identifiers], identifiers)
    linkFile[link] = filename                                                           



with open("output.csv", "w") as file:
    writer = csv.writer(file)      
    flag = 0                                                           
    for rows in originalCsv:
        if flag:
            rows[linkIndex] = linkFile[rows[linkIndex]]                                         # dic structure --> links from original file : filename assigned
        else:
            flag+=1
    for rows in originalCsv:
        writer.writerow(rows)
    
    