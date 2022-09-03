def sol():
    str1=str(input()).lower()
    str2=str(input()).lower()
    if len(str1)>=1 and len(str1)<=100 and len(str2)>=1 and len(str2)<=100:
        if str1==str2:
            return 0
        elif str1<str2:
            return -1
        elif str1>str2:
            return 1



if __name__=='__main__':
    print(sol())
