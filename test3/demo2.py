
from test3.demo1 import Stu
class Col(Stu):
    def __init__(self,name,age):
        super(Col,self).__init__(name,age)

    def do_homework(self,e_score,m_score):
        super(Col,self).e_marking(e_score)
        super(Col,self).m_marking(m_score)
        total = super(Col,self).add(e_score,m_score)
        self.total = total
        super(Col,self).stu_print()
