# encoding= utf-8
'''
    for for/else 
        主要用于 遍历/循环 序列，集合或者字典
'''

a = [[1,2,3],[4,5,6]]
for n in a:
    for m in n:
        if m == 2:
            break # break终止循环
                  # continue暂停循环
        print(m)
else:             # for循环一般不使用else
    print('EOF')