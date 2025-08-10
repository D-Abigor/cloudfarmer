import csv_handler.py as csvm
import downloader.py as dwn

print("before starting please ensure your column containing the links has the heading renamed to 'link/links'")
wait = input()

linkmaps = csvm.processcsv()

import os
folder = "cloudfarmer downloads"
try:
    os.mkdir(folder)
except FileExistsError:
    pass
except OSError as error:
    print(f"unable to generate '{folder}': {error}")
    input()
finally:
    try:
        os.chdir("cloudfarmer downloads")
    except FileNotFoundError:
        print(f"Fatal: '{folder}' not found.")
    except OSError as error:
        print(f"Fatal: Unable to access '{folder}': {e}")

print("folders to store downloads were successfuly created/accessed")

for identifiers in linkmaps:
    dwn.download(linkmaps[identifiers], identifier)
    