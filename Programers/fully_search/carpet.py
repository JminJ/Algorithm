import math

def solution(brown, yellow):
    answer = []
    
    # 전체 size를 구한다
    full = brown + yellow
    
    # yellow가 1일 때 아래 for문과 동일한 처리를 해준다. -> for문 범위 때문에 1은 skip 된다
    if yellow == 1:
        garo = yellow
        if (garo + 2) * (3) == full:
            answer.append(garo+2)
            answer.append(3)
    # 1부터 yellow까지 반복한다.
    for i in range(1, yellow):
        # yellow가 i로 나눠질 경우, 
        if yellow % i == 0:
            # garo는 yellow / i 의 몫이 된다.
            garo = yellow / i
            # (garo + 2) * (i + 2)가 full size와 동일하고
            if (garo + 2) * (i + 2) == full:
                # 가로(garo)의 길이가 세로(i)의 길이보다 크거나 같을 경우
                if garo >= i:
                    # 가로 길이와 세로 길이를 차례대로 answer에 추가한다.
                    answer.append(garo+2)
                    answer.append(i + 2)
    
    return answer
    