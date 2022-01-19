from solution import *

def solution(new_id):
    
    
    #1
    new_id = new_id.lower()
    
    #2
    answer = ''
    for i in new_id:
        if i.isalnum() or i in '-_.':
            answer+=i 
    
    #3
    while '..' in answer:
        answer = answer.replace('..','.')
        
    #4
    answer = answer.strip('.')
    
    #5
    if answer =='':
        answer ='a'
        
    #6
    if len(answer) >15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    
    #7
    while len(answer)<3:
        answer += answer[-1]
    return answer
