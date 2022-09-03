import collections
def count_cher():
    '''
    INPUT: AAABBCC
    OUTPUT: 3
    '''
    #test_str = str(input('Enter String:'))
    test_str="AAABBCC"
    all_freq = collections.Counter(test_str)
    print(all_freq)
    repeated={}
    for key, value in all_freq.items():
        if value>1:
            repeated[key]=value
    return repeated

print(count_cher())
