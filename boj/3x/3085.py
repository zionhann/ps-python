def check():
    global max_

    # row
    for _i in range(n):
        _count = 1
        for _j in range(n - 1):
            if candy[_i][_j] == candy[_i][_j + 1]:
                _count += 1
                max_ = max(max_, _count)
            else:
                _count = 1

    # column
    for _i in range(n):
        _count = 1
        for _j in range(n - 1):
            if candy[_j][_i] == candy[_j + 1][_i]:
                _count += 1
                max_ = max(max_, _count)
            else:
                _count = 1


max_ = 0
n = int(input())
candy = [list(input()) for _ in range(n)]

# row
for i in range(n):
    for j in range(n - 1):
        if candy[i][j] == candy[i][j + 1]:
            continue
        else:
            candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]
            check()
            candy[i][j + 1], candy[i][j] = candy[i][j], candy[i][j + 1]

# column
for i in range(n):
    for j in range(n - 1):
        if candy[j][i] == candy[j + 1][i]:
            continue
        else:
            candy[j][i], candy[j + 1][i] = candy[j + 1][i], candy[j][i]
            check()
            candy[j + 1][i], candy[j][i] = candy[j][i], candy[j + 1][i]

print(max_)

'''
리뷰:
열과 행 따로 순회하는 건 알겠는데
열 또는 행에서 같은 문자가 몇 개인지 판별하는 로직(check() 함수 부분)을 떠올리기 어려웠다.
다른 분들 풀이를 보고 이해하면서 제출했는데도 7번만에 맞았다.

check() 함수에서 인접한 두 사탕을 비교하고 같은 색이 아니면 count를 1로 초기화하는 게 이해가 가지 않았다..
(count는 같은 행 또는 열에서 같은 색이 연속한 개수이다.)
예를 들어 AAB 행에서 처음 AA를 비교할 때는 같은 색이므로 count == 2가 되지만
그 다음 AB를 비교할 때 같지 않다고 해서 count == 1이 되는 것은 납득하기가 어려웠다.

하지만
해당 로직은 필요하다. 
AABB 행의 경우 같은 색이 인접한 최대 개수는 2개이지만 AB를 비교할 때 count 를 1로 초기화를 하지 않으면
BB를 비교할 때 count는 3이 된다.

해결 방법은 행 또는 열에서 인접한 두 사탕의 색을 비교할 때(두번째 반복문)마다 
count와 최대값을 비교하여 대입하는 것이었다.
이렇게 하면 AAB 행에서 AA를 비교할 때 max_ == count == 2가 되므로 이후 AB를 비교해서 count == 1이 되더라도
해당 행의 인접한 같은 색의 최대값은 여전히 2이다.
'''