def solution(clothes):
    answer = 0
    
    c = {}
    
    for i in clothes:
        if i[1] not in c:
            c[i[1]] = 1
        elif i[1] in c:
            c[i[1]] += 1
        
    muls = mul(c.values())
    answer += muls
    
    return answer

def mul(values):
    result = 1
    
    for i in values:
        result *= (i+1)
    result -= 1
    return result