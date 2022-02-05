a, b = map(int, input().split())
c = list(map(int, input().split()))
d = list()

for i in range(a-2):
    for j in range(i+1, a-1):
        for k in range(j+1, a):
            if c[i] + c[j] + c[k] <= b:
                d.append(c[i] + c[j] + c[k])
print(max(d))
