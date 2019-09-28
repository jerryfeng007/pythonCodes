# http://tushare.org/boxoffice.html#id4

import json
import tushare as ts

# df = ts.month_boxoffice()  # 取上一月票房数据
df = ts.month_boxoffice('2019-09')  # 取2015年10月的数据
df = df[0:5]
# print(df)

d = {}
for idx, row in df.iterrows():
    d[idx] = {}
    d[idx]['Irank'] = eval(row['Irank'])
    d[idx]['MovieName'] = row['MovieName']
    d[idx]['avgboxoffice'] = row['avgboxoffice']
    d[idx]['avgshowcount'] = row['avgshowcount']
    d[idx]['boxoffice'] = row['boxoffice']
# print(d)

with open('hello.txt', 'w') as f:
    json.dump(d, f)

with open('hello.txt', 'r') as f:
    dd = json.load(f)
    print(dd)
