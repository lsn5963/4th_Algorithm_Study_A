import math


def solution(k, d):
    answer = 0
    # x 기준으로 세기
    for x in range(0, d + 1, k):
        res_d = math.floor(math.sqrt(d * d - x * x))

        answer += (res_d // k) + 1
        print((res_d // k))
    return answer