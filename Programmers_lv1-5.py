def solution(answers):
    
    answer=[]
    
    #패턴정리
    
    first_supo = [1,2,3,4,5] #5
    second_supo = [2,1,2,3,2,4,2,5] #8
    third_supo = [3,3,1,1,2,2,4,4,5,5] #10
    
    #점수 초기값 설정
    first_score = 0
    second_score = 0
    third_score = 0
    
    for i in range(len(answers)):
        if answers[i] == first_supo[i%5]:
            first_score += 1
        if answers[i] == second_supo[i%8]:
            second_score += 1
        if answers[i] == third_supo[i%10]:
            third_score += 1
    
    
    
    #가장 많이 맞춘 사람. 뽑기
    Max = max(first_score, second_score, third_score)
    
    
    if Max == first_score: answer.append(1)   
    if Max == second_score: answer.append(2)    
    if Max == third_score: answer.append(3)
    
    
    
    
    
    return answer
