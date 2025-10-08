S, P = list(map(int, input().split()))
dna = list(input())
minAlpha  = list(map(int, input().split()))
checkList = [0] * 4
answer = 0
left = 0
right = P-1

def add(c):
    if c == 'A':
        checkList[0] += 1
    elif c == 'C':
        checkList[1] += 1
    elif c == 'G':
        checkList[2] += 1
    elif c == 'T':
        checkList[3] += 1

def remove(c):
    if   c == 'A':
        checkList[0] -= 1
    elif c == 'C':
        checkList[1] -= 1
    elif c == 'G':
        checkList[2] -= 1
    elif c == 'T':
        checkList[3] -= 1

def isPassword():
    for i in range(4):
        if checkList[i] < minAlpha[i]:
            return False
    return True

def init():
    for i in range(P):
        add(dna[i])
        
def main():
    global left, right, answer
    init()
    if isPassword():
        answer += 1
    for i in range(P, S):
        remove(dna[left])
        left  += 1
        right += 1
        add(dna[right])
        if isPassword():
            answer += 1
    print(answer)

main()