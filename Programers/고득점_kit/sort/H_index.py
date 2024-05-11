def solution(citations):
    answer = 0

    # citations의 unique 값들만 list로 만든다
    c_ts = list(set(citations))  
    
    if len(citations) < 2:
        answer = citations[0]
    
    # c_ts의 max값 까지 for문을 돌린다.
    for h in range(max(c_ts)):
        cnt = 0
        # h값과 citations값을 비교
        for i in range(len(citations)):
            # citations[i]값이 h보다 크거나 같으면 cnt에 1을 더한다.
            if citations[i] >= h:
                cnt += 1
        # cnt가 h이상이라면 
        if cnt >= h:
            # cnt가 len(citations-cnt) 이상이라면 
            if cnt >= (len(citations) - cnt):
                # h가 answer 아상이라면 answer를 h로 바꿈
                if answer < h:
                    answer = h
                
    return answer