# 默认参数

def add(name,age = 18,sex = "man"):
    print("I'm " + name)
    print("I'm " + str(age))
    print("I'm " + sex)

add("steven")
print("~~~~~~~~~~~~~~~~~~")
add("james",sex = "woman")

# 可变参数
def demo(*demo):
    print(demo)
    print(type(demo))
print("~~~~~~~~~~~~~~~~~~")
demo(1,2,3,4)
    