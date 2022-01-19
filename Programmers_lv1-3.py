def solution(lottos, win_nums):
    answer = [0,0]
    cnt=0
    ranker=[6,6,5,4,3,2,1]
    zero_cnt=lottos.count(0)
    for i in win_nums:
        if i in lottos: cnt+=1
    answer[0]=ranker[cnt+zero_cnt]
    answer[1]=ranker[cnt]
    
    return answer
