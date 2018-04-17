# 平方和
def squsum(*demo):
    sum = 0
    for i in demo:# 可变参数的遍历
        sum += i*i
    print(sum)
squsum(1,2,3,4)
print('~~~~~~~~~~~~~~~~~~~~~~~~~')

# 关键字可变参数
def city_temp(**temp):
    print(temp)
    print(type(temp))

city_temp(bj = '32c', cd = '23c', sh = '33c')
print('~~~~~~~~~~~~~~~~~~~~~~~~~')

# 字典的遍历
def city(**ds):
    for key,value in ds.items():
        print(key,': ',value)
    for a in ds.keys():
        print(a)
    for b in ds.values():
        print(b)

city(bj = '32c', cd = '23c', sh = '33c')