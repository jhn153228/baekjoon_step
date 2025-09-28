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
