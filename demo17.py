import json
# 反序列化
json_str = '{"name":"ljj", "age":18, "bool":false}' # json object 里面的字符串必须用双引号
json_arr ='[1,9,9,5]' # json array

a = json.loads(json_str)
b = json.loads(json_arr)
print(type(a))
print(a)
print(type(b))
print(b)