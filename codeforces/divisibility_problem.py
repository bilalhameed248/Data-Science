def sol():
    t=int(input())
    if t>=1 and t<=10000:
        a=[]
        b=[]
        for i in range(t):
            x, y=input().split()
            x=int(x)
            y=int(y)
            if x>=1 and y<=1000000000:
                a.append(x)
                b.append(y)
        count=0
        result=[]
        for i in a:
            d=b[count]
            if i%d==0:
                result.append(0)
            else:
                c1=1
                tbd=i
                z=True
                while z!=False:
                    tbd=tbd+1
                    if tbd%d==0:
                        result.append(c1)
                        break
                    else:
                        c1=c1+1
            count = count+1
        return result


if __name__=='__main__':
    result=sol()
    for i in result:
        print(i)
