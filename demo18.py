import json
# 序列化
student = [
            {'name':'ljj', 'age':18, 'bool':False},
            {'name':'ljj', 'age':19}
          ]

json_str = json.dumps(student)
print(type(json_str))
print(json_str)