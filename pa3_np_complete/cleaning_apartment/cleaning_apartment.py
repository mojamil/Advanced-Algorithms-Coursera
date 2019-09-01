# python3
from itertools import combinations
n, m = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(m) ]

# This solution prints a simple satisfiable formula
# and passes about half of the tests.
# Change this function to solve the problem.
def base_clause(n):
    cl=0
    return cl
def get_adjacent(v,edges):
    adjacent=[]
    for e in edges:
        if v in e:
            adjacent+=[i for i in e if i!=v]
    return set(adjacent)
def convert(num,n):
    counter=1
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i*100 + j == num:
                return counter
            if -(i*100+j)== num:
                return -counter
            counter+=1
    return
def printEquisatisfiableSatFormula():
    clauses=[]
    clauses+=[[i*100 + j for j in range(1,n+1)] for i in range(1,n+1)]
    for o in range(1,n+1):
        cl=[j*100 + o for j in range(1,n+1)]
        for pair in combinations(cl, 2):
            if [-pair[1],-pair[0]] not in clauses and [-pair[0],-pair[1]] not in clauses:
                clauses.append([-d for d in pair])
    for o in range(1,n+1):
        for e in range(1,n):
            cl=[-(o*100+e)]
            for j in get_adjacent(o,edges):
                cl.append(j*100+e+1)
            clauses.append(cl)
        
    for e in range(0,len(clauses)):
        for d in range(0,len(clauses[e])):
            clauses[e][d]=convert(clauses[e][d],n)
    # with open('tmp.cnf', 'w') as f:
    #     f.write("p cnf {} {}\n".format(n*n, len(clauses)))
    #     for c in clauses:
    #         c.append(0);
    #         f.write(" ".join(map(str, c))+"\n")
    print(len(clauses),n*n)
    for l in clauses:
        print(" ".join(map(str, l)),0)

printEquisatisfiableSatFormula()
