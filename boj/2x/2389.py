a = int(input())
ans = 0

while a >= 0:
    if a % 5 == 0:
        ans += a // 5
        print(ans)
        break
    else:
        a -= 3
        ans += 1
else:
    print(-1)

'''
리뷰:
쉬어 보이는데 어렵다.
O(N)말고 O(1)로 해결하는 풀이도 있다.
https://st-lab.tistory.com/72
이해하면 큰 도움이 될 것 같다.
'''