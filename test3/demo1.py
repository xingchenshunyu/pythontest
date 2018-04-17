class Stu():
    sum = 0 # 类变量，班级总人数，实例变量控制
    sum1 = 0 # 类方法控制的类变量
    # 类变量和实例变量的区别：
    # 类变量为所有实例共享，实例变量为每个实例独有的

    def __init__(self,name,age):
        # 构造函数 类实例化自动执行
        self.name = name
        self.age = age
        self.e_score = 0
        self.m_score = 0
        self.__class__.sum += 1

    def e_marking(self,e_score):
        if e_score < 0 or e_score > 100:
            print('\n英语成绩不合法\n')
            e_score = 0
        self.e_score = e_score
        print("english: " + str(self.e_score))

    def m_marking(self,m_score):
        if m_score < 0 or m_score > 100:
           print("\n数学成绩不合法\n")
           m_score = 0
        self.m_score = m_score
        print("math: " + str(self.m_score))

    @staticmethod # 装饰器：静态方法的标志
    # 静态方法可以调用类变量但不能调用实例变量
    # 静态方法可以被实例方法和类方法调用
    # 一般不使用静态方法
    def add(a,b):
        c = a + b
        return c

    def stu_print(self):
        print("name: " + self.name)
        print("age: " + str(self.age))
        print("this is static: " + str(Stu.add(self.e_score,self.m_score)))
    
    def stu_score(self):
        score = self.e_score + self.m_score
        return score

    @classmethod # 类方法的标志
    # 类方法不能调用实例变量
    def class_num(cls):
        cls.sum1 += 1
        return cls.sum1




        
        
