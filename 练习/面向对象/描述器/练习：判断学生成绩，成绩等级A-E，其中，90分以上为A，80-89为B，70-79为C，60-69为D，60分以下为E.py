import bisect

def get_grade(score):
    breakpoints = [60, 70, 80, 90]
    grades = 'EDCBA'
    print('index:{}'.format(bisect.bisect(breakpoints, score)))
    return grades[bisect.bisect(breakpoints, score)]

for x in (91, 82, 77, 65, 50, 60, 70):
    print('{} => {}'.format(x, get_grade(x)))