from matplotlib.pyplot import sca
import numpy as np

a = [32,64,128,256,512]
b = [0.5, 1, 2]
c,d = np.meshgrid(np.array(a), np.array(b))
print(c)
print(d)
print(c.shape, d.shape)
print("|=================")
c = c.flatten()
d = d.flatten()
print(c)
print(d)

print(np.sqrt(d))