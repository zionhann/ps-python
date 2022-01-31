a, b = input().split()
print(int(a) + int(b))

'''
여러 변수에 문자를 입력받을 때는 split() 함수를 사용하자.
number를 입력받더라도 input() 함수로 입력 받은 수는 문자로 취급된다.
따라서 print(a + b)를 하더라도 3이 아닌 '12'가 출력된다.

다른 분들의 코드를 보니 map() 함수를 사용했다.
map(int, input().split())
input().split()을 통해 반환된 iterable을 int 함수를 통해 정수형으로
형변환한 결과(iterator)를 반환한다.

'''
