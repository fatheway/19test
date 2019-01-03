# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。

# 1sort排序
l=[]
for i in range(3):
    a=int(input('请输入第%d个整数：\n'%(i+1)))
    l.append(a)
l.sort()
print(l)

#2冒泡处理：
inp = input('请输入3个整数：')
l=inp.split(',')
a=[int(x) for x in l]
print(a)
l=[]
while len(a)>0:
    min=a[0]
    index=0
    for i in range(len(a)):
        if a[i]<min:
            min=a[i]
            index=i
    a.pop(index)
    l.append(min)
print(l)

# 3.冒泡
for i in range(len(a)-1):
    for j in range(len(a)-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)


