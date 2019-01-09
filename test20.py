# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；
# 再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
h=100
tour=[]
height=[]
for i in range(1,11):
    if i==1:
        tour.append(h)
    else:
        tour.append(2*h)
    h/=2
    height.append(h)
print('总高度：{}'.format(sum(tour)))
print('第10次高度：{}'.format(height[9]))