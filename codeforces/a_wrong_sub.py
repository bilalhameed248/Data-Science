def sol():
    n,k = input().split()
    n=int(n)
    k=int(k)

    if n>=2 and n<= 10**9 and k>=1 and k<=50:
        for i in range(k):
            ld=n%10
            if ld!=0:
                n=n-1
            else:
                n=n//10
        return n

if __name__=='__main__':
    print(sol())
