# 구구단
def s_2739():
    n = int(input())
    for i in range(1, 10):
        print(f"{n} * {i} = {n*i}")

# A+B - 3
def s_10950():
    t = int(input())

    for _ in range(t):
        a, b = map(int, input().split())
        print(a + b)

def s_8393():
    sum_num = 0
    n = int(input())
    for i in range(1, n+1):
        sum_num += i
    print(sum_num)

def s_25304():
    total_cost = int(input())
    prev_cost = 0
    n = int(input())
    for i in range(1, n + 1):
        cost, cnt = map(int, input().split())
        prev_cost += cost * cnt
    if total_cost == prev_cost:
        print('Yes')
    else:
        print('No')

def s_25314():
    n = int(input())
    cnt = n // 4
    print('long ' * cnt + 'int')