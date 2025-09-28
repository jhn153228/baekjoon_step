# 프로그래머스 스쿨 2025 코드 챌린지 2차 예선 ( 서버 증설 횟수 )
def solution(players, m, k):
    answer = 0
    servers = []
    for time, player in enumerate(players):
        need_server = player // m
        servers = [s for s in servers if s["delete_time"] != time]

        use_server_cnt = sum(s["create_cnt"] for s in servers)

        if use_server_cnt < need_server:
            create_cnt = need_server - use_server_cnt
            answer += create_cnt
            servers.append({'delete_time': time + k, 'create_cnt': create_cnt})

    return answer


players = [0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 4, 2, 0, 6, 0, 4, 2, 13, 3, 5, 10, 0, 1, 5]
m = 3
k = 5
# solution(players, m, k)

