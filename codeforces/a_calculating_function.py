def sol():
    n=int(input())
    if  n>=1 and n<=10**15:
        if n%2==0:
            return n//2
        else:
            return (((n-1)//2)+1)*-1
if __name__=='__main__':
    print(sol())
