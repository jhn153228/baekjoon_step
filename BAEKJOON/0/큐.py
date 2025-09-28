
def s_15235():
    """
    올림피아드 피자 스택 문
    :return:
    """
    n = int(input())
    pizza_list = list(map(int, input().split()))
    time_list = [0] * n
    _time = 0
    while sum(pizza_list) > 0:
        for idx, i in enumerate(pizza_list):
            if pizza_list[idx] > 0:
                pizza_list[idx] -= 1
                _time += 1
                if pizza_list[idx] == 0:
                    time_list[idx] = _time
    print(*time_list)

def s_2075():
    """
    N * N 의 배열에 숫자가 채워져 있을 때 N번째로 큰 수
    :return:
    """
    import sys, heapq
    n = int(sys.stdin.readline())
    n_rows = []
    for _ in range(n):
        data = list(map(int, sys.stdin.readline().split()))
        for d in data:
            if len(n_rows) < n:
                heapq.heappush(n_rows, d)
            else:
                if n_rows[0] < d:
                    heapq.heappush(n_rows, d)
                    heapq.heappop(n_rows)
    print(n_rows[0])
