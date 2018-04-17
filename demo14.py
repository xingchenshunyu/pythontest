
import re
# \d 数字 \D 非数字
# \w 单词元素 \W 非单词元素
a = 'adlkfjs12kjafklj344kaljflkja344'
s = 'pytho11python12Pythonn13'
q = '522188972'
w = 'pythongojavago'
r = re.findall('[^a-z]',a) # 概况字符串，^表示否,[a-b]范围

r2 = re.findall('[a-z]{7,9}',a) # 数量词 贪婪,{a,b}区间
r3 = re.findall('[a-z]{7,9}?',a) # 数量词 非贪婪
# 正则表达式默认贪婪，在数量词后加？为非贪婪

r4 = re.findall('python*',s)
# * 匹配它前面的字符0次及多次
# + 匹配它前面的字符1次及多次
# ？匹配它前面的字符0次及1次

r5 = re.findall('python*',s,re.I)
# re.I 让正则表达式忽略大小写

r6 = re.findall(r'^\d{7,9}$',q)
# ^前边界，$后边，控制范围

r7 = re.sub('go','ljj',w,0)
# 默认为0，替代多次，可根据需要替代

# print (r2)
# print (r3)
# print (r4)
print (r5)
print (r6)
print (r7)
