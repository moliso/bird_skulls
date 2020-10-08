import pandas as pd
import os
from pathlib import Path

file = 'czaszki_excel.xlsx'

xl = pd.ExcelFile('czaszki_excel.xlsx', engine=None)

dfl = xl.parse(sheet_name='R')

testRow = dfl['scientific_name']

path = '/Users/pioka/Documents/zlecenia UG/Czaszki całoscGZA_715_species_workfiles/aCCIPITERIDAE'

files = os.listdir(path)

fileNamesList = []

for fileName in testRow:
    fileNamesList.append(fileName.lower())


for photoName in files:
    tmp = Path(photoName).stem
    if tmp in fileNamesList:
        print("succes")
    else:
        print(photoName)
