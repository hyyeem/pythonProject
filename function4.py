'''
def add_10(value):
    ''''''value에 10을 더한 값을 돌려주는 함수''''''
    result = value + 10
    return result

n = add_10(42)#함수가 값을 갖도록 한다.
print(n) #출력 : 52

n = round(1.5)
print(n)
'''
##############################
'''
def add_10(value):
    ''''''value에 10을 더한 값을 돌려주는 함수''''''
    print('return 앞')
    return 10 #먼저 나온 return값이 반환된다.
    print('return 뒤')
    result = value + 10
    return result

n = add_10(42)#함수가 값을 갖도록 한다.
print(n) #출력 : 52

n = round(1.5)
print(n)
'''
######################################
'''
def add_10(value):
    ''''''value에 10을 더한 값을 돌려주는 함수''''''
    if value < 10:
        return 10 #즉시 종료
    result = value + 10
    return result

n = add_10(5)
print(n)
n = add_10(42)
print(n)

n = round(1.5)
print(n)
'''
##########################################
'''
def add_10(value):
    ''''''value에 10을 더한 값을 돌려주는 함수''''''
    if value < 10:
        result = 10
    else:
        result = value + 10
    return result

n = add_10(5)
print(n)
n = add_10(42)
print(n)

n = round(1.5)
print(n)
'''
#####################################
'''
def root(a, b, c):
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

    return r1

x = 1
y = 2
z = -8

# a * x^2 + b* x + c = 0, a != 0인 x에 관한 2차 방정식에 대해,
# 근의 공식은

r = root(x, y, z) #실행인자
print('근은 {}'.format(r))
'''
##############################################

def root(a, b, c):
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

    return r1, r2

x = 1
y = 2
z = -8

# a * x^2 + b* x + c = 0, a != 0인 x에 관한 2차 방정식에 대해,
# 근의 공식은

r1, r2 = root(x, y, z) #실행인자
print('근은 {} {}'.format(r1, r2))