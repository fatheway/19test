# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？


# 实现1
for i in range(1,5):
    for j in range(1,5):
        for m in range(1,5):
            if i!=m and i !=j and j!=m:
                print(i,j,m)


# 实现2
for i in range(1,5):
    for j in range(1,5):
        for m in range(1,5):
            if i==m or i==j or j==m:
                continue
            print(i,j,m)