a = int(input())
c = list()
for i in range(a):
    b = tuple(input().split())
    c.append(b)
for i in range(len(c)):
    for j in list(c[i][1]):
        print(j * int(c[i][0]), end='')
    print()

'''
리뷰:
    너무 복잡하게 생각한 것 같다.
    list c를 생성할 것 없이 반복문으로
    문자열 'ABC'에서 각 문자에 대한 곱셈만 처리해주면 되는 문제다.
'''