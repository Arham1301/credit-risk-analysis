import pandas as pd
df = pd.read_excel('raw_cr_loan2.xlsx')
condition = (df['loan_grade'] == 'A') & df['loan_int_rate'].isnull()
condition1 = (df['loan_grade'] == 'B') & df['loan_int_rate'].isnull()
condition2 = (df['loan_grade'] == 'C') & df['loan_int_rate'].isnull()
condition3 = (df['loan_grade'] == 'D') & df['loan_int_rate'].isnull()
condition4 = (df['loan_grade'] == 'E') & df['loan_int_rate'].isnull()
condition5 = (df['loan_grade'] == 'F') & df['loan_int_rate'].isnull()
df.loc[condition, 'loan_int_rate'] = 7.327
df.loc[condition1, 'loan_int_rate'] = 10.99
df.loc[condition2, 'loan_int_rate'] = 13.46
df.loc[condition3, 'loan_int_rate'] = 15.36
df.loc[condition4, 'loan_int_rate'] = 17
df.loc[condition5, 'loan_int_rate'] = 18.689
df.to_excel('clean_raw_cr_loan2.xlsx', index=False, engine='openpyxl')


