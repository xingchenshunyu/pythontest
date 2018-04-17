
from test3.demo1 import Stu

# 第一个实例变量
stu1 = Stu("xiaoming",19)
stu1.stu_print()
stu1.e_marking(70)
stu1.m_marking(-1)
print("Total score: " + str(stu1.stu_score()))
print('当前班级同学人数： ' + str(Stu.sum))
print('类方法控制的班级人数变化： ' + str(Stu.class_num()))
print('\n')
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# 第二个实例变量
stu2 = Stu("honghong",17)
stu2.stu_print()
stu2.e_marking(110)
stu2.m_marking(78)
print("Total score: " + str(stu2.stu_score()))
print('当前班级同学人数： ' + str(Stu.sum))
print('类方法控制的班级人数变化： ' + str(Stu.class_num()))
print('\n')
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print(stu1.__dict__)
print('\n')
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print(Stu.__dict__)
print("\n")
print("this is static: " + str(Stu.add(1,2)))



