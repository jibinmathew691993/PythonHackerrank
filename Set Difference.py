a,b = [set(input().split()) for _ in range(4)][1::2]

print(len(a.difference(b)))