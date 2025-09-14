# 두 수 비교하기
def s_1330():
    A, B = map(int, input().split())
    if A > B:
        print('>')
    elif A < B:
        print('<')
    elif A == B :
        print('==')
def s_9498():
    score = int(input())
    if score >= 90:
        record = 'A'
    elif score >= 80:
        record = 'B'
    elif score >= 70:
        record = 'C'
    elif score >= 60:
        record = 'D'
    else:
        record = 'F'
    print(record)

def s_2753():
    year = int(input())
    if year % 4 == 0 and year % 100 != 0: # 4의 배수이면서 100의 배수가 아닐 때 윤년
        print(1)
    else:
        if year % 400 ==0:
            print(1)
        else:
            print(0)

def s_14681():
    x = int(input())
    y = int(input())

    if x > 0:
        if y > 0:
            print(1)
        else:
            print(4)
    else:
        if y > 0:
            print(2)
        else:
            print(3)

def s_3884():
    from datetime import datetime, timedelta
    hour, minute = map(int, input().split())
    time = datetime(2024,1,1,hour,minute)
    time -= timedelta(minutes=45)
    print(time.hour, time.minute)

def s_2525():
    hour, minute = map(int, input().split())
    from datetime import datetime, timedelta
    cooking_time = int(input())
    time = datetime(2024,1,1,hour,minute)
    time += timedelta(minutes=cooking_time)
    print(time.hour, time.minute)


def s_2480():
    a, b, c = map(int, input().split())
    if a == b == c:
        print(10000 + a * 1000)
    elif a == b or a == c:
        print(1000 + a * 100)
    elif b == c:
        print(1000 + b * 100)
    else:
        print(max(a, b, c) * 100)
