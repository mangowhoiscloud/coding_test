import sys
input = sys.stdin.readline

class Node(object):
    def __init__(self):
        self.terminal = False
        self.children = {}
        self.data = ""

class Trie(object):
    def __init__(self):
        self.parent = Node()

    def insert(self, str):
        here = self.parent
        temp_length = 0
        for char in str:
            if char not in here.children:
                here.children[char] = Node()
            here = here.children[char]
            temp_length += 1
        here.data = str

    def search(self, str):
        here = self.parent
        for char in str:
            if char not in here.children:
                return False
            here = here.children[char]
        
        return here.data == str

n, m = map(int, input().split())
trie = Trie()

for _ in range(n):
    word = input().strip()
    trie.insert(word)

result = 0

for _ in range(m):
    word = input().strip()
    if trie.search(word):
        result += 1

print(result)