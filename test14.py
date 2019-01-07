# 将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

x = int(input("输入正整数："));
while x:
    print("%d="%x,end='')
    if x==1:
        print(x)
    while x not in [1]:
        for i in range(2,x+1):
            if x%i==0:
                x=int(x/i)
                if x==1:
                    print("%d" % i, end='')
                else:
                    print("%d*"%i,end='')
                break
    x=int(input())



