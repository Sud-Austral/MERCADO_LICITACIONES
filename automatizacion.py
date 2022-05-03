import requests as req
import json
import pandas as pd
import datetime
import sys
from zipfile import ZipFile
import os


def getData():
    now = datetime.datetime.now()
    anio = now.strftime("%Y")
    mes = str(int(now.strftime("%m")))
    fecha =  f'{anio}-{mes}'
    URL = f'https://transparenciachc.blob.core.windows.net/lic-da/{fecha}.zip'
    myfile = req.get(URL)
    open('auxiliar_file.zip', 'wb').write(myfile.content)
    test_file_name = "auxiliar_file.zip"
    with ZipFile(test_file_name, 'r') as zip:
        zip.printdir()
        zip.extractall() 
    try:
        os.mkdir(anio)
    except:
        pass
    try:
        os.mkdir(f'{anio}/{mes}')
    except:
        pass
    df = pd.read_csv(f'lic_{fecha}.csv', sep=";")
    df.to_excel(f'{anio}/{mes}/licitacion_{fecha}.xlsx', index=False)
    os.remove(test_file_name)
    os.remove(f'lic_{fecha}.csv')
    return True


if __name__ == '__main__':
    print("Comenzo...")
    getData()
