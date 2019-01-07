# 输出指定格式的日期。

import datetime

# print(datetime.date.today().strftime('%d%m%Y'))

a=datetime.date(1941,1,5)
print(a.strftime('%d-%m-%Y'))
b=a+datetime.timedelta(days=1)
print(b.strftime('%d-%m-%Y'))

c=a.replace(year=a.year+1)
print(c.strftime('%d-%m-%Y'))