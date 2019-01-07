# 题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
a=input('输入一行字符：')
letters=0
space=0
number=0
other=0
for b in a:
    # b=a[i]
    # print(b)
    if b.isalpha():
        letters+=1
    elif b.isspace():
        space+=1
    elif b.isdigit():
        number+=1
    else:
        other+=1
print(f'英文字母{letters}个、空格{space}个、数字{number}个其它字符{other}个')
