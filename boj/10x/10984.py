class CourseInfo:
    def __init__(self, credits_, value):
        self.credits_ = credits_
        self.value = value

    def grade_point(self):
        return self.credits_ * self.value


class GPA:
    def __init__(self, credits_, point):
        self.credits_ = credits_
        self.point = point


result = []
number_of_semesters = int(input())

for i in range(number_of_semesters):
    _sum = 0
    gp = list()
    _list = list()
    _number_of_subjects = int(input())
    for j in range(_number_of_subjects):
        _credits, _value = map(float, input().split())
        _list.append(CourseInfo(_credits, _value))
    for j in _list:
        _sum += j.credits_
        gp.append(j.grade_point())
    result.append(GPA(_sum, sum(gp)/_sum))
for key in result:
    print(f"{int(key.credits_)} {key.point: .1f}")

'''
리뷰:
너무 어렵게 푼 것 같다.
클래스까지 갈 것 없이
이수학점의 합과 '학점*평점'의 합을 변수에 저장하고
소수점 자리만 주의해서 출력하면 더 간단해진다.
'''
