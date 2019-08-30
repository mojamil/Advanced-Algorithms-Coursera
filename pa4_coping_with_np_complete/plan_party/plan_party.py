#uses python3

import sys
import threading

# This code is used to avoid stack overflow issues
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size


class Vertex:
    def __init__(self, weight):
        self.weight = weight
        self.maxw=None
        self.children = []


def ReadTree():
    size = int(input())
    tree = [Vertex(w) for w in map(int, input().split())]
    for i in range(1, size):
        a, b = list(map(int, input().split()))
        tree[a - 1].children.append(b - 1)
        tree[b - 1].children.append(a - 1)
    return tree


def dfs(tree, vertex, parent):
    
    if tree[vertex].maxw==None:
        if  not tree[vertex].children or (tree[vertex].children[0]==parent and len(tree[vertex].children)==1):
            tree[vertex].maxw=tree[vertex].weight
        else:
            # print("vertex:",vertex)
            m1=tree[vertex].weight
            for child in tree[vertex].children:
                # print("children:",tree[vertex].children)
                if child != parent:
                    for gchild in tree[child].children:
                        # print("grandchildren:",tree[child].children)
                        if gchild != child and gchild!= parent and gchild!=vertex: 
                            m1+=dfs(tree, gchild, child)
                            # print("grandchild:",gchild)
                            # print("funf:",m1)
            m0=0
            for child in tree[vertex].children:
                if child != parent:
                    m0+=dfs(tree, child, vertex)
            tree[vertex].maxw=max(m1,m0) 
    return tree[vertex].maxw
    # This is a template function for processing a tree using depth-first search.
    # Write your code here.
    # You may need to add more parameters to this function for child processing.


def MaxWeightIndependentTreeSubset(tree):
    size = len(tree)
    if size == 0:
        return 0
    dw=dfs(tree, 0, -1)
    # You must decide what to return.
    return dw


def main():
    tree = ReadTree();
    weight = MaxWeightIndependentTreeSubset(tree);
    print(weight)


# This is to avoid stack overflow issues
threading.Thread(target=main).start()
