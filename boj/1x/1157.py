word = input().upper()
letters = tuple(set(word))
count = list()

for i in range(len(letters)):
    count.append(word.count(letters[i]))

print(letters[count.index(max(count))] if count.count(max(count)) == 1 else '?')

'''
리뷰:
    한번에 맞긴 했지만 시간이 많이 걸렸다.
    블로그에 정리해서 다시 리뷰하기.
'''