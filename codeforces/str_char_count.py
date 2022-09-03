import collections
from unicodedata import name
def sol():
    '''
    INPUT: AAABBCC
    OUTPUT: 3
    '''
    s = str(input("Enter String:"))
    dist={}
    count=1
    for i in range(len(s)):
        if s[i] not in dist:
           dist[s[i]] = count
        else:
            value=dist[s[i]]
            dist[s[i]]=value+1
    print(dist)
    return max(dist.values())
    

    
if __name__=='__main__':
    print(sol())