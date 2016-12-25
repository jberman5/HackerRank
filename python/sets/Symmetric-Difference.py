m = input()
mSet = set(map(int, input().split()))
n = input()
nSet = set(map(int, input().split()))

diffM = mSet.difference(nSet) # Values which exist in mSet but not in nSet
diffN = nSet.difference(mSet)

symDiff = diffM.union(diffN) # Values which exist in diffM or diffB
pizza = sorted(symDiff)
for index in range(len(symDiff)):
    print(list(pizza)[index])
    
