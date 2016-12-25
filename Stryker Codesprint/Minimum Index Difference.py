total = input()
A = list(map(int, input().split()))
B = list(map(int, input().split()))


i = 0
diff = int(total)+1
while i <= (int(total)-1):
    comp = abs(i-B.index(A[i]))
    if diff > comp:
        diff = comp
        lowPos = i
    if diff == comp:
        if A[lowPos] > A[i]:
            lowPos = i
    i += 1

print(A[lowPos])
