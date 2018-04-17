
import re
a = 'Ling19meng95xi0813'

def th(values):
    a = values.group()
    if int(a) >= 6:
        return str(1)
    else:
        return str(0)

r = re.sub(r"\d",th,a)
print(r)

b = 'l1ing99m508eng81xi3'

def th1(values):
    i = values.group()
    if int(i) >= 50:
        return '100'
    else:
        return '0'

r1 = re.sub(r'\d{2,3}',th1,b)
print(r1)