a = int(input())
list_ = map(int, input().split())
ans = 0

for _ in list_:
    e = 0
    if _ > 1:
        for i in range(2, _):
            if _ % i == 0:
                e += 1
        if e == 0:
            ans += 1
print(ans)

'''
리뷰

https://ooyoung.tistory.com/92
'''