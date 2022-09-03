def sol():
    n=int(input())
    s=str(input()).upper()
    count_a=0
    count_d=0
    if len(s)==n:
        for i in s:
            if i=='A':
                count_a+=1
            elif i=='D':
                count_d+=1
            else:
                return
        if count_a>count_d:
            return "Anton"
        elif count_a<count_d:
            return "Danik"
        else:
            return "Friendship"







if __name__=='__main__':
    print(sol())
