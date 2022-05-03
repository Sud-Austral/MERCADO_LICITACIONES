import requests as req
import json
import pandas as pd
import datetime
import sys
from zipfile import ZipFile


def getData():
    URL = 'https://transparenciachc.blob.core.windows.net/lic-da/2022-5.zip'
    myfile = req.get(URL)
    open('auxiliar_file.zip', 'wb').write(myfile.content)
    test_file_name = "auxiliar_file.zip"
    with ZipFile(test_file_name, 'r') as zip:
        zip.printdir()
        zip.extractall() 
    return True


if __name__ == '__main__':
    print("Comenzo...")
    getData()
