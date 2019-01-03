# 题目：输入某年某月某日，判断这一天是这一年的第几天？
year=int(input('请输入年：'))
mouth=int(input('请输入月：'))
day=int(input('请输入日：'))
d=[0,31,59,90,120,151,181,212,243,373,304,334]
days=d[mouth-1]
sumday = days  + day
fe=0
if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
    fe=1
    if mouth>2:
        sumday+=1

print(sumday)


