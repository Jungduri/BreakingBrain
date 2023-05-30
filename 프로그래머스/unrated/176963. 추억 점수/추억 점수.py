def solution(name, yearning, photo):
    
    score_dict = {n:y for n, y in zip(name, yearning)}
    answer = []

    for photo_set in photo:
        score = 0
        for elem in photo_set:
            if elem in score_dict:
                score+=score_dict[elem]
        answer.append(score)
        
    return answer