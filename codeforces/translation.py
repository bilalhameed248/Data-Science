def sol():
    s=str(input()).lower().strip()
    t=str(input()).lower().strip()
    if len(s)<=100 and len(t)<=100:
        str1=""
        for i in s:
            str1 = i + str1
        if str1==t:
            return "YES"
        else:
            return "NO"

if __name__=='__main__':
    print(sol())
