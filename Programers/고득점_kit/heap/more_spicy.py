import heapq

def solution(scoville, K):
    answer = 0
		# scoville list를 오름차순으로 정렬
    scoville.sort()

		# scoville[0] ==> 최솟값 
    while scoville[0] < K:
        try:
            min_scov = int(heapq.heappop(scoville))
            min_scov += (int(heapq.heappop(scoville))*2)
			      # min_scov가 push 됨(크기에 따라 정렬됨)
            heapq.heappush(scoville, min_scov)
            answer += 1
            # 만약 list내 요소가 하나도 없을 시 IndexError 발생하므로 예외처리
        except IndexError:
            return -1
        
    return answer