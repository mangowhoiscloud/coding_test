idx = 0
n = int(input())
stk = list()
array = list()
result = []

for i in range(n):
    array.append(int(input()))

for number in range(1, n+1):
    if idx >= n:
        break
    if number <= array[idx]:
        stk.append(number)
        result.append("+")
    while len(stk) > 0 and array[idx] == stk[-1]:
        stk.pop()
        result.append("-")
        idx += 1

if len(stk) == 0:
    for c in result:
        print(c)
else:
    print("NO")