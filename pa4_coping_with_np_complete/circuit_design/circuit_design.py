# python3
import sys
import threading
import cProfile
sys.setrecursionlimit(10**6)
threading.stack_size(2**26)
import math
n, m = map(int, input().split())
clauses = [ list(map(int, input().split())) for i in range(m) ]

# This solution tries all possible 2^n variable assignments.
# It is too slow to pass the problem.
# Implement a more efficient algorithm here.

# revd=dict([reversed(i) for i in d.items()])
# d.update(revd)
def main():
    def create_implication(clauses):
        graph={}
        for c in clauses:
            if -c[0] not in graph.keys():
                graph[-c[0]]=set([c[1]])
            else:
                graph[-c[0]].add(c[1])
            if -c[1] not in graph.keys():
                graph[-c[1]]=set([c[0]])
            else:
                graph[-c[1]].add(c[0])
        nodes=list(range(-n,n+1))
        nodes.remove(0)
        d=dict()
        for i, item in enumerate(nodes):
            d[item]=i
        return graph,list(nodes),d

    G,N,rdi=create_implication(clauses)

    stid=0
    ids=[-1]*len(N)
    lowlinks=[0]*len(N)
    onst=[False] * len(N)
    st=[]
    
    def tarjan(g,n):
        for i in n:
            k=rdi[i]
            if ids[k]==-1:
                dfs(k,g,n)
        return lowlinks
    assigments=[None]*n
    def dfs(i,g,n):
        nonlocal st
        nonlocal stid
        st.append(i)
        onst[i]=True
        lowlinks[i]=stid
        ids[i]=lowlinks[i]
        stid+=1
        if n[i] in g.keys():
            for link in g[n[i]]:
                link=rdi[link]
                if ids[link]==-1:
                    dfs(link,g,n)
                    lowlinks[i]=min(lowlinks[i],lowlinks[link])
                elif onst[link]:
                    lowlinks[i]=min(lowlinks[i],ids[link])
        if ids[i]==lowlinks[i]:
            scc=set()
            while st[len(st)-1]!=i:
                w=st.pop()
                onst[w]=False
                lowlinks[w] = ids[i]
                scc.add(w)
                if not assigments[abs(N[w])-1]:
                    assigments[abs(N[w])-1]=N[w]
            w=st.pop()
            onst[w]=False
            lowlinks[w] = ids[i]
            if not assigments[abs(N[w])-1]:
                    assigments[abs(N[w])-1]=N[w]
    def isSatisfiable():
        t=tarjan(G,N)
        for i in range(0,int(len(N)/2)):
            if t[i]==t[i+2*abs(N[i])-1]:
                return None
        return assigments
    # pr = cProfile.Profile()
    # pr.enable()
    result = isSatisfiable()
    # pr.disable()
    # pr.print_stats()
    if result is None:
        print("UNSATISFIABLE")
    else:
        print("SATISFIABLE")
        print(" ".join([str(r) for r in result]))
threading.Thread(target=main).start()
