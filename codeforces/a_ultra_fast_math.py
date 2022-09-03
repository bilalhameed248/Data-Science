def sol():
    x=input()
    y=input()
    x = [int(a) for a in str(x)]
    y = [int(b) for b in str(y)]
    if len(x) == len(y):
        count=0
        result=[]
        for i in x:
            if i==y[count]:
                result.append(0)
            else:
                result.append(1)
            count=count+1
        return ''.join([str(elem) for elem in result])

if __name__=='__main__':
    print(sol())
