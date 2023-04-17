edges_data='''0 0 38 95 0 1 57 0
0 0 0 0 79 0 36 19
38 0 0 51 0 0 44 0
95 0 51 0 0 44 0 0
0 79 0 0 0 93 41 48
1 0 0 44 93 0 1 0
57 36 44 0 41 1 0'''

data=[[int(x) for x in line.split()]for line in edges_data.split('\n')]
n=len(data)
e=[]

for i in range(n):
    for j in range(i+1,n):
        w=data[i][j]
        if w>0:
            e.append((i,j,w))

c=list(range(n))
m=[]
while len(m)<n-1:
    z=[None]*n
    for u,v,w in e:
        a=c[u]
        b=c[v]
        if a!=b:
            if z[a] is None or z[a][2]>w:
                z[a]=u,v,w
            if z[b] is None or z[b][2]>w:
                z[b]=u,v,w
    for i in range(n):
        if z[i] is not None:
            u,v,w=z[i]
            a=c[u]
            b=c[v]
            if a!=b:
                m.append((u,v,w))
                for j in range(n):
                    if c[j]==b:
                        c[j]=a

def boruvka(e,c,n,m):
    while len(m)<n-1:
        z=[None]*n
        for u,v,w in e:
            a=c[u]
            b=c[v]
            if a!=b:
                if z[a] is None or z[a][2]>w:
                    z[a]=u,v,w
                if z[b] is None or z[b][2]>w:
                    z[b]=u,v,w
        for i in range(n):
            if z[i] is not None:
                u,v,w=z[i]
                a=c[u]
                b=c[v]
                if a!=b:
                    m.append((u,v,w))
                    for j in range(n):
                        if c[j]==b:
                            c[j]=a
    return m

print(boruvka(e,c,n,m))
