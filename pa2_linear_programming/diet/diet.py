# python3
from sys import stdin
import math
import numpy as np
EPS = 1e-3
def conneg(l):
  if len(l)==0:
    return False
  num=min(l)
  if num<0:
    return num
  else:
    return False
def find_pivot(A,b,c,B):
  tc=[]
  for ind in range(0,len(c)):
    if ind not in B:
      tc.append(c[ind])
  negest=conneg(tc)
  col=0
  if negest:
    col=c.index(negest)
    ratios=[]
    rati=[]
    for i in range(len(A)):
      if A[i][col]>0:
        ratios.append(b[i]/A[i][col])
        rati.append(i)

    if len(ratios)==0:
      return (-1,-1)
    row=rati[ratios.index(min(ratios))]
    return (row,col)
  else:
    return False


def find_basis(A):
  basis=[0]*len(A)
  for col in range(0,len(A[0])):
    ocount=0
    zcount=0
    for row in range(0,len(A)):
      if A[row][col]==1:
        oneloc=row
        ocount+=1
      if A[row][col]==0:
        zcount+=1
    if ocount==1 and zcount==len(A)-1:
      basis[oneloc]=col
  return basis

def solve_diet_problem(n, m, A, b, c,Art):  
  # Write your code here

  B=find_basis(A)
  b+=[0]*(len(B)-len(b))
  cb=[]
  for bas in B:
    cb.append(c[bas])
  cz=[]
  zj=[]
  for z in range(0,len(c)):
    yi=[]
    for j in range(0,len(A)):
      yi.append(A[j][z])
    zj.append(sum([a*b for a,b in zip(cb,yi)]))
    cz.append(sum([a*b for a,b in zip(cb,yi)])-c[z])
  piv=find_pivot(A,b,cz,B)
  itere=0
  # if not piv:
  #   print("Art:",Art)
  #   print("pivot:",piv)
  #   print("b:",b)
  #   print("B:",B)
  #   print("Cb:",cb)
  #   print("A:",np.matrix(A))
  #   print("Z:",zj)
  #   print("Zj-Cj:",cz)
  while piv:
    # print("Art:",Art)
    # print("pivot:",piv)
    # print("b:",b)
    # print("B:",B)
    # print("Cb:",cb)
    # print("A:",np.matrix(A))
    # print("Z:",zj)
    # print("Zj-Cj:",cz)
    if piv==(-1,-1):
      return [1,[]]
    pival=A[piv[0]][piv[1]]
    for el in range(0,len(A[piv[0]])):
      A[piv[0]][el]=A[piv[0]][el]/pival

    b[piv[0]]=b[piv[0]]/pival
    for row in range(0,len(A)):
      if row!=piv[0]:
        multiplier=A[row][piv[1]]
        subtractor=[a*multiplier for a in A[piv[0]]]
        A[row]=[a-b for a,b in zip(A[row],subtractor)]
        b[row]-=b[piv[0]]*multiplier
    multiplier=cz[piv[1]]/pival
    subtractor=[a*multiplier for a in A[piv[0]]]
    B[piv[0]]=piv[1]
    cb[piv[0]]=c[piv[1]]
    cz=[]
    zj=[]
    for z in range(0,len(c)):
      yi=[]
      for j in range(0,len(A)):
        yi.append(A[j][z])
      zj.append(sum([a*b for a,b in zip(cb,yi)]))
      cz.append(sum([a*b for a,b in zip(cb,yi)])-c[z])
    tr=-1
    for j in Art:
      
      if j not in B:
        #print("j",j)
        A=[a[:j]+a[j+1:] for a in A]
        cz.pop(j)
        zj.pop(j)
        c.pop(j)
        tr=j
    #print("B:",B)     
    if tr>=0:
      #print(tr)
      index=Art.index(tr)
      if index==0:
        Art=[a-1 for a in Art]
        for r in Art:
          if r+1 in B and r+1>tr:
            B[B.index(r+1)]-=1
      elif index<len(Art)-1:
        for r in range(index,len(Art)):
          Art[r]=Art[r]-1
        for r in Art:
          if r+1 in B and r+1>tr:
            B[B.index(r+1)]-=1
      Art.pop(index)  
    piv=find_pivot(A,b,cz,B)
    itere+=1
  sol=[]
  # print(B)
  # print(b)
  
  for i in range(0,len(A[0])):
    if i in B:
      sol.append(b[B.index(i)])
    else:
      sol.append(0)
  #print(sol)
  return [0, sol[:m]]

def feasiblity_test(A,b,c,sol):
  feasible=True
  for i in range(len(A)):
    multiplied=[a*b for a,b in zip(A[i][:len(sol)],sol)]
    if sum(multiplied)>b[i] and not math.isclose(sum(multiplied),b[i],rel_tol=EPS):
      feasible=False
      break
  return feasible
n, m = list(map(int, stdin.readline().split()))
A = []
Aorg=[]
for i in range(n):
  l=[0]*(n)
  l[i]=1
  A += [list(map(int, stdin.readline().split()))+l]
  Aorg+= [A[i]]
b = list(map(int, stdin.readline().split()))
borg=b.copy()
c = list(map(int, stdin.readline().split()))
l=[0]*(n)
c+=l
Art=[]
for i in range(len(b)):
  if b[i] < 0:
    b[i]*=-1
    A[i]=[a*-1 for a in A[i]]
    Art.append(len(A[i]))
    A[i]+=[1]
    for j in range(len(A)):
      if j!=i:
        A[j]+=[0]
    c+=[-1000000000000]
anst, ansx = solve_diet_problem(n, m, A, b, c,Art)
if not feasiblity_test(Aorg,borg,c,ansx) and anst==0:
   anst=-1
if anst == -1:
  print("No solution")
if anst == 0:  
  print("Bounded solution")
  print(' '.join(list(map(lambda x : '%.18f' % x, ansx))))
if anst == 1:
  print("Infinity")
    
