import openpyxl

import pandas as pd

import requests
import json

#################################################################
print("Get CIIV Actividad")


df = pd.read_excel('CIIU.xlsx', sheet_name = [f'ciiv'])

content={}
data_array=[]


        # "model": "a_bank.filetypes",
        # "pk": 1,
        # "fields": {
        #     "name": "Captaciones",
        #     "code": "CA01"
        # }

for table in df.values():
    for row in table.iterrows():
        data_dict={}
        data_dict['fields']={}
        data_dict['model'] = 'a_bank.activity'
        data_dict['fields']['code_ciiv'] = row[1].CIIU
        data_dict['fields']['macro'] = row[1].Macro
        data_dict['fields']['activity'] = row[1].Actvidad

        data_dict['fields']['DP1'] = ''        
        if str(row[1].DP1) != 'nan':
            data_dict['fields']['DP1'] = row[1].DP1

        data_dict['fields']['DP2'] = ''
        if str(row[1].DP2) != 'nan' :
            data_dict['fields']['DP2'] = row[1].DP2

        data_dict['fields']['DP3'] = ''
        if str(row[1].DP3) != 'nan':
            data_dict['fields']['DP3'] = row[1].DP3

        data_dict['fields']['R1'] = ''        
        if str(row[1].R1) != 'nan':
            data_dict['fields']['R1'] = row[1].R1

        data_dict['fields']['R2'] = ''
        if str(row[1].R2) != 'nan' :
            data_dict['fields']['R2'] = row[1].R2

        data_dict['fields']['R3'] = ''
        if str(row[1].R3) != 'nan':
            data_dict['fields']['R3'] = row[1].R3


        data_array.append(data_dict)
        

content= data_array
json_object  =  json.loads(json.dumps(content,indent=4))
with open('ciiv_actividad_data.json', 'w') as f:
    json.dump(json_object,f,indent=4)

print('DONE')        