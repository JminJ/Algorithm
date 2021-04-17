from itertools import permutations
import math

def solution(numbers):
    answer = 0
    
    numbers = list(numbers)

    # 문자열 조합을 1부터 len(number)까지의 범위로 계산 ex) i = 2, 'AB','BC','CD' | i = 3, 'ABC','DEF','GHJ'...
    for i in range(1,len(numbers)+1):
        # input list의 순열 구하기 
        new_nums = list(set(map(''.join, permutations(numbers, i))))
        ps = process(new_nums)
        answer += ps
    
    return answer

def process(new_nums):
    cnt = 0
    
    for i in range(len(new_nums)):
        # 소수인지 아닌지를 current_val % i를 통해 결과가 0이라면 1을 더하므로 판별한다.(마지막까지 0이면 소수, 0보다 크면 소수가 아님)
        t_f = 0
        # 순열에서 '01','011'...등을 뛰어넘는다. -> 중복이 되기 때문 
        if new_nums[i][0] == '0':
            continue
        current_val = int(new_nums[i])
        # current_val이 0 또는 1이라면 뛰어넘는다.
        if current_val < 2 :
            continue
        
        # current_val의 제곱근(루트)를 계산하고 올림을 해 정수형으로 바꿔준다.
        val = math.ceil(math.sqrt(current_val))
        # val 까지 계산하기 위해 종료 범위를 val +1로 설정한다.
        for j in range(2, val+1):
            # current_val이 2와 같다면 무조건 소수로 판단 -> for문이 2부터 시작하므로 나눠지게 된다.
            if current_val == 2:
                break
            # current_val이 j로 나눠지면 t_f에 1을 더한다.
            if (current_val % j) == 0:
                t_f += 1
                break
        if t_f == 0:
            cnt += 1
        
    return cnt