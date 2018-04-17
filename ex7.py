
def distance():
    x = 0
    def step(a):
        nonlocal x
        x = x + a
        return x
    return step

dis = distance()
print(dis(2))
print(dis(3))
    