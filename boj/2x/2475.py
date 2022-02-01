result = 0
a = map(int, input().split())
for i in a:
    result += pow(i, 2)
print(result % 10)

'''
리뷰:
list comprehension을 사용해서 나타내보자.
pow() 함수 대신 'x**2' 형식으로 제곱을 나타낼 수 있다.

A compact way to process all or part of the elements in a sequence and return a list with the results.
result = ['{:#04x}'.format(x) for x in range(256) if x % 2 == 0] 
generates a list of strings containing even hex numbers (0x..) 
in the range from 0 to 255. The if clause is optional. 
If omitted, all elements in range(256) are processed.
(https://docs.python.org/3/glossary.html#term-list-comprehension)
'''