def sol():
    s=str(input())
    if len(s)>=1 and len(s)<=100:
        lower_count=0
        upper_count=0
        for i in s:
            if(i.islower()):
                lower_count=lower_count+1
            elif(i.isupper()):
                upper_count=upper_count+1
        if lower_count > upper_count:
            return s.lower()
        elif lower_count < upper_count:
            return s.upper()
        else:
            return s.lower()



if __name__=='__main__':
    print(sol())
