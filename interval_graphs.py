import sys
from collections import deque 
input_filename=sys.argv[2]
g = {}
with open(input_filename) as graph_input:
    for line in graph_input:
        nodes = [int(x) for x in line.split()]
        if len(nodes) != 2:
            continue
        if nodes[0] not in g:
            g[nodes[0]] = []
        if nodes[1] not in g:
            g[nodes[1]] = []
        g[nodes[0]].append(nodes[1])
        g[nodes[1]].append(nodes[0])
def lexbfs(g):
    s=[{x for x in g.keys()}]
    s1=[]
    sn=[x for x in g.keys()]
    lex = []
    i = 0
    neigh=[]
    og=[]
    while sn:
        lex.insert(i,next(iter(s[0])))
        s[0].remove(lex[i])
        i=i+1
        neigh= []
        og = []
        for x in s:
                for y in x:
                    if len(x)==1:
                            k=x
                            s1.append(k)
                    else:
                        if y in g[lex[len(lex)-1]]:
                                neigh.append(y)      
                        else:
                                og.append(y) 
                if len(neigh)!=0:
                    s1.append(neigh)
                if len(og)!=0:    
                    s1.append(og)
                neigh=[]
                og=[]   
                s=s1.copy()         
        s1=[]
        del sn[0] 
    return lex
def chordal(graph,order):
    rnu=set()
    rnv=set()
    flag=False
    flag_list=[]
    order =order[::-1]
    x=[]
    for u in order:
        flag=False
        x=order[order.index(u) + 1:]
        if len(graph[u])!=0:
                for r in x:
                    if r in graph[u]:
                        v=r
                        break
                valuei=order.index(u)
                new_list=order[valuei+1:]
                for y in new_list:
                    if y in graph[u]:
                        rnu.add(y)              
                value2=order.index(v)
                w=order[value2+1:]
                for t in w:
                    if t in graph[v]:
                        rnv.add(t)
                if len(rnv)==0:
                    flag=True
                if len(rnu)!=0:
                    if v in rnu:
                        rnu.remove(v)
                if rnu.issubset(rnv):
                    flag=True
        flag_list.append(flag)
        rnu=set()
        rnv=set()
        if False in flag_list:
            return False
    return True              
def nbfs(g,node,order):
    q = deque()
    path=[]
    i=0
    visited = [ False ] * len(g)
    inqueue = [ False ] * len(g)
    q.appendleft(node)
    inqueue[node] = True
    while not (len(q) == 0):
        c = q.pop()
        path.insert(i,c)
        i=i+1
        inqueue[c] = False
        visited[c] = True
        for v in g[c]:
            if not visited[v] and not inqueue[v] and v in order:
                q.appendleft(v)
                inqueue[v] = True      
    return path
def bfs(g: dict, node: int):
    components=[]
    i=0
    q = deque()
    
    visited = [ False ] * len(g)
    inqueue = [ False ] * len(g)
    
    q.appendleft(node)
    inqueue[node] = True
    
    while not (len(q) == 0):
        c = q.pop()
        if c!=node and c not in g[node]:
            components.insert(i,c)
        i=i+1
        inqueue[c] = False
        visited[c] = True
        for v in g[c]:
            if not visited[v] and not inqueue[v] :
                q.appendleft(v)
                inqueue[v] = True     
    return components
def atfree(g):
    answer= chordal(g,lexbfs(g))
    if answer==True:
        max_node = max(g.keys())
        table = [[None for _ in range(max_node+1)] for _ in range(max_node+1)]
        content=[]
        s=0
        r=0
        for x in g.keys():
            new_list=bfs(g,x)
            for u in g.keys():
                table[u][u]=0
                for v in g.keys():
                    if v in g[u]:
                        table[u][v]=0 
                for zi in g.keys() :
                    if table[x][zi]==None:
                        #print(s,len(alph))
                        table[x][zi]=nbfs(g,zi,new_list)
                        s=s+1  
        def results(g):
            flag = False  
            for u in g.keys():
                for v in g.keys():
                    for w in g.keys():
                        if table[u][v] != 0 and table[u][w] != 0 and table[v][u] != 0 and table[v][w] != 0 and table[w][u] != 0 and table[w][v] != 0:
                            if sorted(table[u][v]) == sorted(table[u][w]) and sorted(table[v][u]) == sorted(table[v][w]) and sorted(table[w][u]) == sorted(table[w][v]):
                                flag = True  
                                break  
                    if flag:
                        break  
                if flag:
                    break 
            if flag:
                return False
            else:
                return True
        return results(g)
    else:
        return False
if sys.argv[1]=="lexbfs":
    print(lexbfs(g))
if sys.argv[1]=="chordal":
    print(chordal(g,lexbfs(g)))
if sys.argv[1]=="interval":
    print(atfree(g))
 
                      
               


        
            
        




    






