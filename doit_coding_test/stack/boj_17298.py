n = int(input())
array = list(map(int, input().split()))
stk = []
answer = [-1] * n
startIdx = 0
endIdx = 0

for i in range(n):
    if len(stk) == 0:
        stk.append(i)
        continue
    number = array[i]
    while len(stk) > 0 and array[stk[-1]] < number:
        idx = stk[-1]
        answer[idx] = number
        stk.pop()
    stk.append(i)

print(answer)