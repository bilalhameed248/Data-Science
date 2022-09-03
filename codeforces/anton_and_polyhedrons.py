def sol():
    n = int(input())
    if n>=1 and n<= 200000:
        score=0
        dist1={'Tetrahedron':4, 'Cube':6, 'Octahedron':8, 'Dodecahedron':12,'Icosahedron' :20}
        for i in range(n):
            x=str(input())
            if x in dist1:
                score=score+dist1[x]
        return score



if __name__=='__main__':
    print(sol())
