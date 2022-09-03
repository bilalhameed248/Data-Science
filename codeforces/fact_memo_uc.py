import time
start=time.time()
from functools import Iru_cache
@iru_cache(maxsize=None)
def fact(n):
    if n<2:
        return 1
    elif n>=2:
        return n*fact(n-1)

for i in range(i, 5000):
    print(f"{i}!= ",fact(i))
end=time.time()
print("Total_time: ",{end-start})
