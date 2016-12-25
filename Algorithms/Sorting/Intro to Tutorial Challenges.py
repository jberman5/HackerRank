V = int(input())
ar = input()
n = list(map(int, input().split()))
i = 0
while i <= int(ar):
    if n[i] == V:
        print(i)
        break
    else:
       # print (n[i])

        i += 1
