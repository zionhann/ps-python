n = 9
list_ = [int(input()) for _ in range(n)]

for i in range(n-1):
    for j in range(i+1, n):
        if sum(list_) - (list_[i] + list_[j]) == 100:
            for k in sorted(list_):
                if k == list_[i] or k == list_[j]:
                    continue
                print(k)
            exit()

'''
리뷰:
임의의 난쟁이 두 명을 고르는 모든 경우의 수를 구하는 로직이 생각이 안 났다.
1등 코드는 
임의의 난쟁이 두 명의 키의 합 == 9명 키의 합 - 100이면
해당하는 난쟁이의 키 요소를 삭제하고 리스트를 출력한다.  
'''