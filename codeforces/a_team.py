def sol():
    n=int(input())
    first=[]
    second=[]
    third=[]
    result=0
    if n>=1 and n<=1000:
        for i in range(n):
            x, y, z = input().split()
            x=int(x)
            y=int(y)
            z=int(z)
            if x==0 or x==1 and y==0 or y==1 and z==0 or z==1:
                first.append(x)
                second.append(y)
                third.append(z)
        for i in range(len(first)):
            if first[i]==1 and second[i]==1 or first[i]==1 and third[i]==1 or second[i]==1 and third[i]==1:
                    result = result+1
        return result








if __name__=='__main__':
    print(sol())
