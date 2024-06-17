import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


file_path = 'data cleaning/clean_raw_cr_loan2.xlsx'

df = pd.read_excel(file_path)
a = df.to_dict(orient='records')
k1=0
L=[]
L1=[]
L2=[]
while (k1>=0 and k1<=1) :
 for k in ['A','B','C','D','E','F']:
   yes = 0
   no = 0
   count = 0
   count1 = 0
   money = 0
   default = 0
   gained = 0

   for i in a:
        if(i["loan_percent_income"]>k1 and i["loan_percent_income"]<(k1+0.05) and ( i["loan_grade"]== k ) ):

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

   gain=gained-default
   if money!=0:
    percent_gain = (gain/money) *100

    L.append(ord(k)*10)
    L1.append(k1)
    L2.append(percent_gain)
 k1=k1+0.05
print(L)
print(L1)
print(L2)
colors = []
for l2 in L2:
    if l2 < -25:
        colors.append('darkred')
    elif l2 < 0 and l2>=-25:
        colors.append('red')
    elif l2 < 5:
        colors.append('green')
    elif l2>=5:
        colors.append('darkgreen')
plt.scatter(L, L1, c=colors, s=100)
plt.xlabel('Loan Grade')
plt.ylabel('Loan to Income Ratio')
plt.title(' Percentage return to bank from different category of customers ')
plt.show()








