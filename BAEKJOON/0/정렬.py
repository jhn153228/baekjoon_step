
def s_11399():
    """
    그리디 알고리즘
    """
    n = int(input())
    time_list = list(map(int, input().split()))
    time_list.sort()
    total_time = 0
    sum_time = 0
    for p in range(n):
        sum_time += time_list[p]
        total_time += sum_time
    print(total_time)

