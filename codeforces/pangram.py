import string
def sol():
    n=int(input())
    s=str(input()).lower()
    
    lower_string = string.ascii_lowercase
    lc_alp_list = list(lower_string)
    if len(s)==n:
        for i in s:
            if i in lc_alp_list:
                lc_alp_list.remove(i)
        if len(lc_alp_list)==0:
            return "YES"
        else:
            return "NO"

if __name__=='__main__':
    print(sol())
