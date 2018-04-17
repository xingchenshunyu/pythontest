
import numpy as np
list_x = [(0, 0), (1, 3), (2, -2)]
x = np.array(list_x)
print(x)
y = x.sum(axis=0)
print(y)