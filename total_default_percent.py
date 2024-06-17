import pandas as pd
import numpy as np

file_path = 'data cleaning/raw_cr_loan2.xlsx'

df = pd.read_excel(file_path)
a = df.to_dict(orient='records')
yes=0
no=0
for i in a:
    for key in i.keys() :
        if(i["cb_person_default_on_file"]=='Y'):
            yes=yes+1
        if(i["cb_person_default_on_file"]=='N'):
            no=no+1
print(yes)
print(no)