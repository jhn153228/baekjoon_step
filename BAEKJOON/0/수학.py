def s_9610():
    import sys
    n = int(sys.stdin.readline())
    Q1 = 0
    Q2 = 0
    Q3 = 0
    Q4 = 0
    AXIS = 0
    for i in range(n):
        x,y = map(int, sys.stdin.readline().split())
        if x > 0 and y > 0:
            Q1 += 1
        elif x < 0 and y > 0:
            Q2 += 1
        elif x > 0 and y < 0:
            Q4 += 1
        elif x < 0 and y < 0:
            Q3 += 1
        elif x ==0 or y == 0:
            AXIS += 1
    print(f"Q1: {Q1}")
    print(f"Q2: {Q2}")
    print(f"Q3: {Q3}")
    print(f"Q4: {Q4}")
    print(f"AXIS: {AXIS}")

def s_2869():
    """
    달팽이 문제
    top 도착일을 x라고 가정했을 때
    도착 하루전 날(x-1) 까지는 (up - down) 반복
    도착 일(x)에는 오로지 up
    (x-1)(up-down) + up >= top
    (x-1)(up-down) >= top - up
    x-1 >= (top-up) / (up-down)
    x >= { (top-up) / (up-down) } + 1
    x >= { (top-up) / (up-down) } + { (up-down) / (up-down) }
    x >= { top - down / up-down }
    """
    up, down, top = map(int, input().split())
    x = (top-down) / (up-down)
    if x == int(x):
        print(int(x))
    else:
        print(int(x) + 1)