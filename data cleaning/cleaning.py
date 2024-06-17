import pandas as pd
file='raw_cr_loan2.xlsx'
f=pd.read_excel(file)
count =0
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
count13=0
dict={}
a =f.to_dict(orient='records')
for i in a :
    for key,value in i.items() :
        if(pd.isna(value)):
            count=count+1
            if(key=='person_age') :
                dict[key] = count1+1
                count1 = count1 + 1
            if (key == 'person_income'):
                dict[key] = count2+1
                count2 = count2 + 1
            if (key == 'person_home_ownership'):
                dict[key] = count3+1
                count3 = count3 + 1
            if (key == 'loan_intent'):
                dict[key] = count4+1
                count4 = count4 + 1
            if (key == 'loan_grade'):
                dict[key] = count5+1
                count5 = count5 + 1
            if (key == 'loan_amnt'):
                dict[key] = count6+1
                count6 = count6 + 1
            if (key == 'loan_int_rate') :
                dict[key] = count7+1
                count7 = count7 + 1
            if (key == 'loan_status') :
                dict[key] = count8+1
                count9 = count9 + 1
            if (key == 'loan_percent_income'):
                dict[key] = count10+1
                count10 = count1 + 1
            if (key == 'cb_person_default_on_file'):
                dict[key] = count11+1
                count11 = count11 + 1
            if (key == 'cb_person_cred_hist_length'):
                dict[key] = count12+1
                count12 = count12 + 1
            if (key == 'person_emp_length'):
                dict[key]=count13+1
                count13=count13+1
print(dict)
print(count)
