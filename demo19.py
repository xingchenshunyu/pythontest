
from enum import Enum
from enum import IntEnum # 枚举标签名后的值必须为int型


class VIP(Enum):
    # 枚举中标识最好大写
    # 枚举的标签名不能重复，但标签下的值可以相同，第二个名称是第一个名称的别称
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4

print(VIP.YELLOW)# 打印标签名称而不是数值，这是枚举的意义
# 枚举和字典及普通类的区别
#   1.字典和普通类键值可变
#   2.普通类没有防止相同标签的功能
#   3.枚举有保护措施，标签和值不能更改
for v in VIP:
    print(v) # 枚举可用for循环遍历 