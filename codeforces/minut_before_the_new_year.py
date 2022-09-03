def sol():
    t=int(input())
    if t>=1 and t<=1439:
        h=[]
        m=[]
        for i in range(t):
            h1, m1 =input().split()
            h1=int(h1)
            m1=int(m1)
            if h1>=0 and h1<=24 and m1>=0 and m1<60:
                h.append(h1)
                m.append(m1)
        result=[]
        count=0
        for i in h:
            hour=23-i
            hour=hour*60
            minut=60-m[count]
            minut=minut+hour
            result.append(minut)
            count=count+1
        return result

if __name__=='__main__':
    result=sol()
    for i in result:
        print(i,"\n")
