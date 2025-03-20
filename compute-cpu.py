import numpy as np
size = 8192 * 8192
maxcount=64
ncount=0
print(f"start {maxcount}")
while ncount<maxcount:
  array = np.random.random(size).astype(np.float32)
  result = np.sort(array)
  ncount=ncount+1
print("done.")
