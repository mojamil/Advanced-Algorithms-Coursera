# python3
from itertools import combinations

n, m = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(m) ]

# This solution prints a simple satisfiable formula
# and passes about half of the tests.
# Change this function to solve the problem.
def convert(num,n):
    counter=1
    for i in range(1,n+1):
        for j in range(1,4):
            if i*10 + j == num:
                return counter
            if -(i*10+j)== num:
                return -counter
            counter+=1
    return

def base_clause(n):
    cl=[[i*10 + j for j in range(1,4)] for i in range(1,n+1)]
    return cl
def get_adjacent(v,edges):
    adjacent=[]
    for e in edges:
        if v in e:
            adjacent+=[i for i in e if i!=v]
    return set(adjacent)
def printEquisatisfiableSatFormula():
    clauses=[]
    clauses+=base_clause(n)
    for o in range(1,n+1):
        cl=[o*10+j for j in range(1,4)]
        for pair in combinations(cl, 2):
            if [-pair[1],-pair[0]] not in clauses and [-pair[0],-pair[1]] not in clauses:
                clauses.append([-d for d in pair])
    for o in range(1,n+1):
        for p in get_adjacent(o,edges):
            for j in range(1,4):
                pair=[-(o*10+j),-(p*10+j)]
                if [pair[1],pair[0]] not in clauses and [pair[0],pair[1]] not in clauses:
                    clauses.append(pair)
    for e in range(0,len(clauses)):
        for d in range(0,len(clauses[e])):
            clauses[e][d]=convert(clauses[e][d],n)
    # with open('tmp.cnf', 'w') as f:
    #     f.write("p cnf {} {}\n".format(n*3, len(clauses)))
    #     for c in clauses:
    #         c.append(0);
    #         f.write(" ".join(map(str, c))+"\n")
    print(len(clauses),n*3)
    for l in clauses:
        print(" ".join(map(str, l)),0)

printEquisatisfiableSatFormula()
