def sol():
    #t=int(input())
    c=[]
    t=128
    for i in range(t):
        #my_input=int(input())
        #c.append(my_input)
        c.append(i)
    result=[]
    for l in range(len(c)):
        if c[l] % 7==0:
            result.append(c[l])
        else:
            first=c[l]
            second=c[l]
            for j in range(1,8):
                first = first+1
                second = second-1
                first_rem = first % 7
                second_rem = second % 7
                if first_rem == 0 and first > 9:
                    print("first Loop")
                    result.append(first)
                    break
                elif second_rem == 0 and second > 9:
                    print("second Loop")
                    result.append(second)
                    break

    return result
                
if __name__=='__main__':
    for i in sol():
        print(i)




