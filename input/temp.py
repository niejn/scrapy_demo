import pandas as pd

df = pd.read_excel('./客户名单（服务器托管）.xlsx')
df = df.apply(pd.to_numeric, errors='ignore')
df['资金账号']
# for i, d in df.iterrows():
#     print(i, d)

for i in df['资金账号']:
    t = str(i)
    print(t)