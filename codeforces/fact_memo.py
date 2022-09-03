import time
start= time.time()
def fact_memo(n):
    fact_dict={}
    if n<2:
        return 1
    if n not in fact_dict:
        fact_dict[n]=n*fact_memo(n-1)
    return fact_dict[n]


for i in range(1,500):
    print(f"{i}! = ", fact_memo(i))
end=time.time()
print("Time= ",{end-start})
