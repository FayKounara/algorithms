import sys
s1=0
s2=0
s3=0
s4=0
def sistades_elements(t):
    count=0
    for x in t:
        if isinstance(x,tuple):
            count+=sistades_elements(x)
        else:
            count+=1
    return count
with open(sys.argv[2]) as f:
    data=f.read()
    r=data.split()
#sorted list from the elements of the file
for i in range(len(r)):
    r[i]=int(r[i])
r.sort()
def distance(x,y):
    if sys.argv[1]== "single":
       s1=0.5
       s2=0.5
       s3=0
       s4=-0.5
    if sys.argv[1]=="complete":
        s1=0.5
        s2=0.5
        s3=0
        s4=0.5
    if isinstance(x,int)and isinstance(y,int):
        return abs(x-y)
    else:
        if isinstance(x,int):
            if sys.argv[1]=="average":
                return (sistades_elements([y[0]])/(sistades_elements([y[0]])+sistades_elements([y[1]])))*distance(x,y[0])+(sistades_elements([y[1]])/(sistades_elements([y[0]])+sistades_elements([y[1]])))*distance(x,y[1])-0*abs(distance(x,y[0])-distance(x,y[1]))
            elif sys.argv[1]=="ward":
                return ((sistades_elements([y[0]])+sistades_elements([x]))/(sistades_elements([y[0]])+sistades_elements([y[1]])+sistades_elements([x])))*distance(x,y[0])+((sistades_elements([y[1]])+sistades_elements([x]))/(sistades_elements([y[0]])+sistades_elements([y[1]])+sistades_elements([x])))*distance(x,y[1])-(sistades_elements([x]))/(sistades_elements([y[0]])+sistades_elements([y[1]])+sistades_elements([x]))*distance(y[0],y[1])
            else:
                return s1*distance(x,y[0])+s2*distance(x,y[1])+s4*abs(distance(x,y[0])-distance(x,y[1]))+s3*distance(y[0],y[1])
        else:
            if sys.argv[1]=="average":
                return (sistades_elements([x[0]])/(sistades_elements([x[0]])+sistades_elements([x[1]])))*distance(y,x[0])+(sistades_elements([x[1]])/(sistades_elements([x[0]])+sistades_elements([x[1]])))*distance(y,x[1])-0*abs(distance(y,x[0])-distance(y,x[1]))
            elif sys.argv[1]=="ward":
                return (sistades_elements([x[0]])+sistades_elements([y]))/(sistades_elements([x[0]])+sistades_elements([x[1]])+sistades_elements([y]))*distance(y,x[0])+((sistades_elements([x[1]])+sistades_elements([y]))/(sistades_elements([x[0]])+sistades_elements([x[1]])+sistades_elements([y])))*distance(y,x[1])-(sistades_elements([y]))/(sistades_elements([y])+sistades_elements([x[0]])+sistades_elements([x[1]]))*distance(x[0],x[1])
            else:
                return s1*distance(y,x[0])+s2*distance(y,x[1])+s4*abs(distance(y,x[0])-distance(y,x[1]))+s3*distance(x[0],x[1])
f=0
#dist contains the distances from one sistada with all the others
while len(r)!=1:
    dist=[]
    d=[]
    q=0
    s=0
    b=[]
    t=[]
    # calculate the distance of all sistades with each other and find min
    while q<int(len(r)):
        for i in range(len(r)):
            dist.insert(i,distance(r[q],r[i]))
            i=i+1
        d=list(dist)
        dist.sort()
        a=dist[1]
        c=d.index(a)
        #insert in t as a tuple the sistades with the minimum distance
        t.insert(s,(r[q],r[c]))
        dist=[]
        #b is synchronised with t and has the distances of the sistades in t
        b.insert(s,d[c])
        s=s+1
        q=q+1
    copy_b=list(b)
    b.sort()
    g=b[0]
    f=copy_b.index(g)
    r.pop(f)
    r[f]=t[f]
    #the following lines are only for the represantation, in order to access the numbers avoiding showing tuples
    new_list=[]
    def show(x):
        for y in x:
            if isinstance(y,tuple):
                show(y)
            else:
                new_list.append(y)
        
        return new_list
    n=[]
    for  i in t[f]:
        n=show([i])
    i=0
    a=[]
    s=0
    while i<sistades_elements([t[f][0]]):
        a.insert(s,n[i])
        a.sort()
        s=s+1
        i=i+1
    print("({})".format(" ".join(str(i) for i in a)),"({})".format(" ".join(str(i) for i in n[sistades_elements([t[f][0]]):])),format(g,".2f"),sistades_elements(t[f]))   
    
    
    







