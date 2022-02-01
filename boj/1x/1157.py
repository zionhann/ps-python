a = input().upper()
b = tuple(set(a))
c = list()

for i in range(len(b)):
    c.append(a.count(b[i]))

print(b[c.index(max(c))] if c.count(max(c)) == 1 else '?')

'''
리뷰:
    한번에 맞긴 했지만 시간이 많이 걸렸다.
    블로그에 정리해서 다시 리뷰하기.
'''