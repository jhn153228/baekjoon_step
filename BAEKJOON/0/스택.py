def s_10773():
    """
    0을 부르면 전에 기록한 숫자를 지운다.
    :return:
    """
    import sys
    k = int(sys.stdin.readline())
    int_list = []
    for i in range(1, k + 1):
        n = int(sys.stdin.readline())
        if n == 0:
            int_list.pop()
        else:
            int_list.append(n)
    print(sum(int_list))