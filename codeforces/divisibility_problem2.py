def sol():
    t=int(input())
    if t>=1 and t<=10000:
        result=[]
        for i in range(t):
            x, y=input().split()
            x=int(x)
            y=int(y)
            if x>=1 and y<=1000000000:
                if x%y==0:
                    result.append(0)
                else:
                    c1=1
                    tbd=x
                    z=True
                    while z!=False:
                        tbd=tbd+1
                        if tbd%y==0:
                            result.append(c1)
                            z=False
                            break
                        else:
                            c1=c1+1
                    print("Iteration for ",i," is ", c1)
        return result


if __name__=='__main__':
    result=sol()
    for i in result:
        print(i)
