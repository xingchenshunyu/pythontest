
import time

def print_time(func):
    def wrapper(*args, **kw):
        print(time.time())
        func(*args, **kw)
    return wrapper

@print_time
def f1(func):
    print('this is the first func named ' + func)

@print_time
def f2(func1,func2):
    print('this is the first func named ' + func1)
    print('this is the first func named ' + func2)

@print_time
def f3(func1,func2,**func3):
    print('this is the first func named ' + func1)
    print('this is the first func named ' + func2)
    print(func3)

f1('test1')
f2('test2', 'test3')
f3('test3', 'test4', a = 1, b = 'a')