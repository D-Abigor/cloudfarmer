import os
import csv
import sys

def processcsv():
    files = os.listdir()
    csvs = ()
    for file in files:                              #traversing filenames to add csv files to csvs
        print(file, file[-3:])
        if file[-3:] == "csv":
            csvs += (file,)
    
    if not csvs:                                    # checking if csv files were found
        print("no csv files were found.")
    else:
        newestFile = max(csvs, key=os.path.getmtime)
        print("the newest file has been detected as", newestFile)
        choice = input("please confirm to proceed(y/Y):")       # getting user confirmation for detected file
        if choice in "yY":
            print("processing...")
            return getlinks(newestFile),newestFile                         # processing the csv file to obtain the links that need to be downloaded and returning it to the original function call
        else:
            print("u may try opening and closing the file u want to harvest")
            sys.exit()

def getlinks(file):
    with open(file, "r") as data:
        reader = csv.reader(data)
        linkMaps = {}                                          # dictionary that is being used to store [unique identifier -> link] pairs
        flag = 0                                               # flag is used for skipping the first heading column
        SN = 0                                                 # in case unique identifiers are not present in the csv file, a new column is created with sequential serial numbers
        for rows in reader:
            if flag:                                           # skipping heading row
                if keys:                                       # if a unique identifier was found, the identifier found is used to associate the extracted links to the row
                    linkMaps[rows[keys]] = rows[linkindex]     # adding entries to linkmaps by referencing each row and using the indexes obtained from the heading row to accurately form key-value pairs
                else:
                    SN+=1                                      # sequentially updating serial numbers if a unique identifier was not found
                    linkMaps[SN] = rows[linkindex]             # adding entries to linkmaps by referencing each row and using the indexes obtained from the heading row to accurately form key-value pairs
                    
            else:
                index = -1                                     # counteracting index errors
                for columns in rows:
                    index+=1
                    if columns.lower() == "name" or columns.lower() == "S.N":    # finding if a unique identifier exists
                        keys = index
                        break
                    else:
                        keys = None                                              # labelling keys as None to signify now unique identifier exists
                    if columns.lower() in "links":
                        linkindex = index                                        # extracting index position for the column with the links
                flag+=1
    return linkMaps

