import sys
input = sys.stdin.readline

formula = list(map(str, input().split("-")))
ans = 0

for i in range(len(formula)):
    numbers = list(map(int, formula[i].split("+")))
    if i == 0:
        ans += sum(numbers)
    else:
        ans -= sum(numbers)
print(ans)