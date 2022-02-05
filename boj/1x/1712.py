a, b, c = map(int, input().split())
if b >= c:
    print(-1)
else:
    print(a // (c - b) + 1)

# a + b * n < c * n
# a < c * n - b * n
# a < n(c - b)
# a/(c - b) < n