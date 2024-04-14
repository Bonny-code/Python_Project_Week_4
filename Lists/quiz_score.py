
quiz_score = [8, 4, 10, 9, 7]

quiz = int(input('Which quiz did you retake '))
index = quiz - 1
score = int(input('What was your score on quiz 2 '))



quiz_score[index] = score
print(quiz_score)
