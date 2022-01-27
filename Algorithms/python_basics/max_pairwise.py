pairs = [5,4,3,3,9]
result = 0



for pair in pairs:
    for sub_pair in pairs:
        if pair != sub_pair:
            if result < pair * sub_pair:
                result = pair * sub_pair

print(result)

res = 0

for FIdx in range(len(pairs)):
    for SIdx in range(len(pairs)):
        if FIdx != SIdx:
            if res < pairs[FIdx] * pairs[SIdx]:
                res = pairs[FIdx] * pairs[SIdx]


print(res)