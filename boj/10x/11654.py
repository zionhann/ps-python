a = input()
print(ord(a))

'''
리뷰:
chr() 함수는 유니코드 값을 파라미터로 받아서
해당 값에 해당하는 문자열을 반환하고

ord() 함수는 하나의 유니코드 문자를 파라미터로 받아서
해당 문자에 해당하는 유니코드 값(integer)을 반환한다.
*문자열의 길이가 2 이상인 경우 TypeError 발생.

Given a string representing one Unicode character, 
return an integer representing the Unicode code point of that character. 
For example, ord('a') returns the integer 97 and ord('€') (Euro sign) returns 8364. 
This is the inverse of chr().
(https://docs.python.org/3/library/functions.html#ord)
'''