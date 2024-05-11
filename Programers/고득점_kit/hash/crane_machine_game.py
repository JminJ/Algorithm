def solution(board, moves):
    answer = 0
    case = []
    
    cnt = -1
    for i in moves:
        cnt += 1
        for j in range(len(board)):
            # print(board[j])
            if board[j][i-1] != 0:
                case.append(board[j][i-1])
                board[j][i-1] = 0
                # print(case)
                
                l = len(case)
                if l >= 2:
                    if case[l-1] == case[l-2]:
                        del case[l-1]
                        del case[l-2]
                            
                        answer += 2
                break
            # print(case)
            # print(answer)
    
    return answer