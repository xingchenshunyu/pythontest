# encoding: utf-8
'''
    条件控制 —— snippet(片段)，嵌套分支，代码块
'''

# snippet

# if condition:
#     pass(占位语句/空语句)
# else:
#   if condition:(嵌套分支)
#     pass
#   else:
#     pass

'''
    elif
'''
a = input()
if a == '1':
    print('app')
elif a == '2':
    print('org')
elif a == '3':
    print('ban')
else:
    print('shopping')
