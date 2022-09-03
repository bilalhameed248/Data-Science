def sol():
    t=int(input())
    c=[]
    for i in range(t):
        my_input=int(input())
        c.append(my_input)
    result=[]
    for l in range(len(c)):
        if c[l] % 7==0:
            result.append(c[l])
        else:
            first=c[l]
            second=c[l]
            for j in range(1,8):
                first = first+1
                second=second-1
                if first % 7==0:
                    result.append(first)
                    break
                elif second%7==0:
                    result.append(second)
                    break
 
    return result
                
if __name__=='__main__':
    for i in sol():
        print(i)
 
 