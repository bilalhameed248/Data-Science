def generator(l):
    l=next(item for item in l)
    print(l)

if __name__=='__main__':
    mylist=[{'name':'bilal','lname':'hameed'},{'name':'farhan','lname':'ahmed'},{'name':'asfand','lname':'shahid'},{'name': 'zahid','lanme':'hameed'}]
    generator(mylist)
    generator(mylist)
