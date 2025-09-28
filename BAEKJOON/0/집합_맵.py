def s_26069():
    """
    총총댄스 문제
    """
    n = int(input())
    dancer = {'ChongChong'}
    for i in range(n):
        a, b = map(str, input().split())
        if a in dancer:
            dancer.add(b)
        elif b in dancer:
            dancer.add(a)
    print(len(dancer))