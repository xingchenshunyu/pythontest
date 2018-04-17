# encoding: utf-8
#!/usr/bin/env python3
'''
    用户名和密码识别
'''

# 所有常量都要大写表示
ACCOUNT = "root"
PASSWORD = "root"

print('please input account')
user_acount = input()
print('please input password')
user_password = input()

if ACCOUNT == user_acount and PASSWORD == user_password:
    print('successful')
else:
    print('failed')
