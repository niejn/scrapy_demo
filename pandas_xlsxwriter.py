import pandas as pd

df1 = pd.DataFrame({'Data': [10, 20, 30, 40]})
df2 = pd.DataFrame({'Data': [13, 24, 35, 46]})

writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')

df1.to_excel(writer, sheet_name='Sheet1')
df2.to_excel(writer, sheet_name='Sheet1', startrow=6)