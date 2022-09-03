def sol():
    w = int(input())
    if w>=1 and w<=100:
        c=[]
        result=[]
        for i in range(w):
            word = str(input())
            word=word.lower()
            c.append(word)
        for j in range(len(c)):
            if len(c[j]) >= 1 and len(c[j]) <= 100:
                if len(c[j]) <= 10:
                    result.append(c[j])
                else:
                    str1=c[j]
                    remaning_char_count= str(len(str1)-2)
                    str2=str1[0]+remaning_char_count+str1[-1]
                    result.append(str2)
        return result

if __name__=='__main__':
    result=sol()
    for i in result:
        print(i)
