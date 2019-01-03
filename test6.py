# 题目：斐波那契数列  斐波那契数列（Fibonacci sequence），又称黄金分割数列，
# 指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
# 在数学上，费波那契数列是以递归的方法来定义：

def fib(n):
    if n==1:
        return 0
    if  n==2:
        return 1
    if n>2:
        return  fib(n - 1) + fib(n - 2)
for i in range(10):
    print(fib(i+1))

# 循环
# a=0
# b=1
# l=[]
# for i in range(10):
#     l.append(a)
#     a,b=b,a+b
# print(l)
