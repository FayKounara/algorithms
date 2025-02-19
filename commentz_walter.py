from collections import deque
import sys
arg2 = sys.argv[1]
if arg2 != "-v":
    arg2 = None
if arg2 is not None:
    args = sys.argv[2:]
else:
    args = sys.argv[1:]
filename=args[len(args)-1]
args.pop(args.index(filename))
args3 = [x[::-1] for x in args]  
length = [len(x) for x in args3]
pmin = min(length)
trie={}
numbers=[]
final=deque()
with open(filename) as file:
    t= file.read()
# insert the words to the trie and give every letter a unique number
def insert(trie, word,count):
    root = trie
    for x in word:
        if x not in root:
            root[x] = {}
            numbers.append(x)
            final.append([root[x].keys()])
            count=count+1
        root = root[x]
    root["#"] = True
    return count,numbers,final
count=1
numbers=[]
table = []
for x in args3:
    count,numbers,final=insert(trie,x,count)
#numbers array has the letters from the words that we search(the letters that are in the trie)
#count the number of nodes
#final the letters that are assigned to every node for 0 in this example a,b
new_dict={}
#put the children from the root
final.appendleft([trie.keys()])
for x in range(len(final)):
    new_dict[x]=list(final[x][0])
#new dict same as final but also assign numbers to the nodes
# array the node that represent the end of the words
array=[]
for x,y in new_dict.items():
    if '#' in y:
        array.append(x)
node={}
copy=numbers[:]
f=1
unique=[]
#unique: assign to every letter a number
for x in range(len(numbers)):
    unique.append(f)
    f=f+1
def find(element,array):
    for x in array:
        if element<x:
            return x     
def search(element,index_v,alist): 
    s_element=[]
    for i in range(len(alist)):
        if alist[i]==element and i>=index_v:
            s_element.append(i)
    return s_element
bfs_d={}
letters={}
#node a representation of the trie without nested dictionairies
#bfs_d:for every node the numbers of the nodes that are neighbors, help for calculating bfs and depth
#letters:for every node the letters that are assigned to it
for x,y in new_dict.items():
    node[x]=[]
    bfs_d[x]=[]
    letters[x]=[]
    k=0
    flag=False
    if len(y)>=2:
        for z in y:
            if flag==False:
                node[x].append([unique[copy.index(z)],z])
                bfs_d[x].append(unique[copy.index(z)])
                letters[x].append(z)
                k=unique[copy.index(z)]
                copy[copy.index(z)]=""
                flag=True
            else:
                c=find(k,array)
                mi=search(z,c,copy)   
                if mi!=[]:
                    if "#" in new_dict[c]:
                       if mi[0]==unique[c] and len(mi)>1:
                            mi[0]=mi[1]
                    node[x].append([unique[mi[0]],z])
                    bfs_d[x].append(unique[mi[0]])
                    letters[x].append(z)
                    k=unique[mi[0]]
                    copy[mi[0]]=""
                else:
                    a=array[array.index(c)-1]
                    node[x].append([unique[a],z])
                    bfs_d[x].append(unique[a])
                    letters[x].append(z)
                    k=unique[a]
                    copy[a]=""

    else:
        if "#" not in y[0]:
            p=copy.index(y[0])
            node[x].append([unique[p],y[0]])
            bfs_d[x].append(unique[p])
            letters[x].append(y[0])
            copy[p]=""
        else:
            node[x].append([])
line=[]
def bfs(g: dict) -> list[bool]:
    depth=[-1] * len(g) 
    node=0
    q = deque()
    depth[node]=0
    visited = [ False ] * len(g)
    inqueue = [ False ] * len(g)
    
    q.appendleft(node)
    inqueue[node] = True
    
    while not (len(q) == 0):
        c = q.pop()
        line.append(c)
        inqueue[c] = False
        visited[c] = True
        for v in g[c]:
            if not visited[v] and not inqueue[v]:
                q.appendleft(v)
                inqueue[v] = True 
                depth[v]=depth[c]+1    
    depth.pop(0)
    return line,depth
place,dep=bfs(bfs_d)
#place: the order of bfs
#dep: the depth of every node(without node 0)
#diff:get the different strings
diff=set(numbers)  
rt=[]
flag=False
numbers2=numbers[:]
for x in diff:
    help_rt=[]
    for y in numbers2:
        if y==x:
            help_rt.append(dep[(numbers2.index(y))])
            numbers2[numbers2.index(y)]=""
    help_rt.sort()
    rt.append([help_rt[0],x])
#failure
failure=[-1]*len(bfs_d.keys())
for x in bfs_d[0]:
    failure[x]=0
failure[0]=0
place.pop(0)
for s in place:
    u=s
    for k in node[s]:
        if k!=[]:
            v=k[0]
            c=k[1]
            ut=failure[u]
            for x in node[ut]:
                if x!=[]:
                    if c==x[1]:
                        failure[v]=x[0]
                    else:
                        while ut!=0:
                            ut=failure[ut]
                            for x in node[ut]:
                                if x!=[]:
                                    if c==x[1]:
                                        failure[v]=x[0]
                if failure[v]==-1:
                        failure[v]=0
#calculations for set1,set2,s1,s2
u=-1
set1=[[]*u for _ in range(len(node))]
set2=[[]*u for _ in range(len(node))]
s1=[[]*u for _ in range(len(node))]
s2=[[]*u for _ in range(len(node))]
fail=failure[:]
while u!=len(node):
    u=u+1
    fail=failure[:]
    for z in fail:
        if z==u:
            set1[u].append(fail.index(z))
            if u!=0:
                s1[u].append(dep[fail.index(z)-1]-dep[u-1])
            fail[fail.index(z)]=-1
s1[0]=[1]
s2[0]=[pmin]
for x in set1[1:]:
    for y in x:
        if y in array:
            set2[set1.index(x)].append(y)
            s2[set1.index(x)].append(dep[y-1]-dep[set1.index(x)-1])
u=-1
w=-1
def f_dict(value):
    for key, val in bfs_d.items():
        for y in val:
            if y == value:
                return key
u=-1
for x in s1:
   if x!=[]:
    s1[s1.index(x)]=min(x)
for x in s2:
   if x!=[]:
    s2[s2.index(x)]=min(x)
u=-1
for x in s1:
    u=u+1
    if s1[u]!=[]:
        s1[u]=min(pmin,s1[u])
    else:
        s1[u]=pmin
u=-1
for x in s2:
    u=u+1
    if u!=0:
        k=f_dict(u)
        if s2[u]!=[]:
            s2[u]=min(s2[k],s2[u])
        else:
                s2[u]=s2[k]
#main code
i=pmin-1
j=0
u=0
m=""
q=deque()
while i<len(t):
    while t[i-j] in letters[u]:
        u=bfs_d[u][letters[u].index(t[i-j])]
        m=m+t[i-j]
        j=j+1
        if u in array:
            q.append([m[::-1],i-j+1])
    if j>i:
        j=i    
    for p in rt:
        if p[1]==t[i-j]:
            w=p[0]
    if w==-1:
        w=pmin+1
    s=min(s2[u],max(s1[u],w-j-1))
    i=i+s
    j=0
    u=0
    m=" " 
if arg2!=None:
    for u in range(len(s1)):
        print(u,":",s1[u],",",s2[u])
for x in q:
    print(x[0],":",x[1])
