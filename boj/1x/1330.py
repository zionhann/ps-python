a, b = map(int, input().split())

if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print('==')

'''
리뷰:
Conditional expressions 로도 나타낼 수 있다.
=> print('>' if a > b else ('<' if a < b else '=='))
(https://www.acmicpc.net/source/16515483)
 
or_test ["if" or_test "else" expression]
(https://docs.python.org/3/reference/expressions.html#conditional-expressions)
'''