import pandas as pd
import numpy as np

file_path = 'data cleaning/clean_raw_cr_loan2.xlsx'

df = pd.read_excel(file_path)
a = df.to_dict(orient='records')
yes=0
no=0
count=0
count1=0
money=0
default=0
gained=0
for i in a:
    for key,value in i.items() :
        if(i["loan_percent_income"]>=0 and ( i["loan_grade"]== 'D' or i["loan_grade"]== 'E'or  i["loan_grade"]== 'F')) :
            money=money+i["loan_amnt"]
            if(pd.isna(i["loan_int_rate"])):
                count1=count1+1
            else :
              money = money + i["loan_amnt"]
              count=count + i["loan_int_rate"]
              if(i["cb_person_default_on_file"] =='Y'):
                default = default + i["loan_amnt"]
                yes=yes+1
              if (i["cb_person_default_on_file"] == 'N'):
                  gained=gained+((i["loan_amnt"]*i["loan_int_rate"])/100)
                  no=no+1
print("Percentage defaults in the dataset are :")
print(yes/(yes+no) *100)
gain=gained-default
percent_gain = (gain/money) *100
print(f"Money gained is {gain}")
print(f"Percentage default is {percent_gain}")









