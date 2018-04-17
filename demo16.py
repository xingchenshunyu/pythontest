import re
a = 'Ling19meng95xi0813'

r = re.match(r'\d',a)# match方法从开始位置匹配，如果开始位置匹配失败则返回空
r1 = re.search(r'\d',a)# search方法搜索整个字符串，返回第一个匹配结果
# match和search一旦匹配到结果立即返回
""" 
与findall的不同
    1.findall返回的是列表，match和search返回值为对象（需要用group方法截获具体内容）
    2.match和search只会进行一次匹配，无论成功与否都会立即返回结果 
"""
print(r)
print(r1) 