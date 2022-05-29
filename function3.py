#함수는 실행인자로 전달받은 x, y, z를 함수를 정의할 때 사용한 매개변수인 a, b, c로 순서대로 연결
'''
def print_sqrt(a, b, c):# 함수 이름(매개변수)
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

    print('해는 {} 또는 {}'.format(r1, r2))

x = 1
y = 2
z = -8

# a * x^2 + b* x + c = 0, a != 0인 x에 관한 2차 방정식에 대해,
# 근의 공식은

print_sqrt(x, y, z) #실행인자

x = 2
y = -6
z = -8

#한번 더 구하려면

print_sqrt(x, y, z) #실행인자
'''
##########################################3

def print_round(number):
    rounded = round(number) #반올림 함수
    print(rounded)

print_round(4.6)
print_round(2.2)
print_round(3.6)
