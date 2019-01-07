# 题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
# 例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
# from functools import  reduce
# a=int(input('请输入数字：'))
# b=int(input('请输入有几个数相加：'))
# s=0
# l=[]
# for i in range(b):
#     s+=a
#     a=a*10
#     l.append(s)
#     print(s)
# sum=reduce(lambda  x,y:x+y,l)
# print(f'计算和为：{sum}')

a=int(input('请输入数字：'))
b=int(input('请输入有几个数相加：'))
s=0
t=0
for i in range(b):
    c=a*10**i
    s += c
    t+=s
    print(s)
print(t)