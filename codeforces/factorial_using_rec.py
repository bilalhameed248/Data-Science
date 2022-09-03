def fac(x):
    if x==1:
        return x
    else:
        return x*fac(x-1)

print(fac(5))