from functools import reduce

list_x = [0,1,2,3,4,5,6]
list_y = [0,2,3,4,5,6,7]
list_x1 = [(0,0),(1,3),(2,-2)]

 
def add(x,y):
    return x+y

print(add(1,2))

f = lambda x,y: x + y # 匿名函数
print(f(1,2))

r = map(lambda x, y:x + y, list_x, list_y) # map，映射
print(list(r))
 
c = ()
def add2(x,y):
    c = map(lambda x,y:x + y,x,y)
    return (c)

r1 = reduce(add2, list_x1) # reduce  
print(list(r1))

r2 = filter(lambda x:True if x > 3 else False, list_x) # filter，过滤，函数里需返回一个布尔值
print(list(r2))