import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

btree = {}

n = int(input())
root = "A"

for _ in range(n):
    here, left, right = input().split()
    btree[here] = [left, right]


def preorder(here):
    print(here, end="")
    for child in btree[here]:
        if child == ".": continue
        preorder(child)

def inorder(here):
    if btree[here][0] != ".":
        inorder(btree[here][0])
    print(here, end="")
    if btree[here][1] != ".":
        inorder(btree[here][1])

def postorder(here):
    for child in btree[here]:
        if child == ".": continue
        postorder(child)    
    print(here,end="")

preorder(root)
print()
inorder(root)
print()
postorder(root)

