def solution(prices):
    answer = []
    
    for i in range(len(prices)):
        answer.append(0)
        # print('answer :',answer)
        for j in range(i+1, len(prices)):
            # print('i = {}, j = {}'.format(prices[i], prices[j]))
            
            if prices[i] > prices[j]:
                if answer[i] == 0:
                    answer[i] = 1
                else:
                    answer[i] += 1
                break
                
            elif prices[i] <= prices[j]:
                answer[i] += 1
                
            else:
                break
    
    return answer