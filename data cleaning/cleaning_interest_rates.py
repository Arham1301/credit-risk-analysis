import pandas as pd
file="raw_cr_loan2.xlsx"
f=pd.read_excel(file)
a =f.to_dict(orient='records')
count=0
count1=0
count2=0
count3=0
count4=0
count5=0
count6=0
count7=0
count8=0
count9=0
count10=0
count11=0
count12=0
sum1=0
sum2=0
sum3=0
sum4=0
sum5=0
sum6=0

dict={}
for i in a:
    for j,value in i.items():
        if(j=='loan_int_rate'):
          if(pd.isna(value)):
              if(i['loan_grade'] == 'A'):
                  count1=count1+1
              if (i['loan_grade'] == 'B'):
                  count2 = count2 + 1
              if (i['loan_grade'] == 'C'):
                  count3 = count3 + 1
              if (i['loan_grade'] == 'D'):
                  count4 = count4 + 1
              if (i['loan_grade'] == 'E'):
                  count5 = count5 + 1
              if (i['loan_grade'] == 'F'):
                  count6 = count6 + 1
          else :
              if (i['loan_grade'] == 'A'):
                  sum1=sum1+value
                  count7=count7+1
              if (i['loan_grade'] == 'B'):
                  sum2 = sum2 + value
                  count8 = count8 + 1
              if (i['loan_grade'] == 'C'):
                  sum3 = sum3 + value
                  count9 = count9 + 1
              if (i['loan_grade'] == 'D'):
                  sum4= sum4 + value
                  count10 = count10 + 1
              if (i['loan_grade'] == 'E'):
                  sum5 = sum5 + value
                  count11 = count11 + 1
              if (i['loan_grade'] == 'F'):
                  sum6 = sum6 + value
                  count12 = count12 + 1

dict['A']=count1
dict['B']=count2
dict['C']=count3
dict['D']=count4
dict['E']=count5
dict['F']=count6
avgA=sum1/count7
avgB=sum2/count8
avgC=sum3/count9
avgD=sum4/count10
avgE=sum5/count11
avgF=sum6/count12
print(dict)
print(avgA)
print(avgB)
print(avgC)
print(avgD)
print(avgE)
print(avgF)

