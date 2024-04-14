# each student took 3 quiz's
quiz_score = {'Al': [8, 9, 5], 'Bettina': [6, 10, 10], 'Cody': [7, 7, 9]}

# loop
for student, list_of_scores in quiz_score.items():
    print(f'student {student} scores are {list_of_scores}')

# how to get 1 list
cody_scores = quiz_score['Cody']

# the enumerate function will number the list
for i, score in enumerate(cody_scores):
    print(f'on quiz {i+1} Cody scored {score}')

# to get maximun scores we use the mx keyword
cody_max = max(cody_scores)
print(f'Cody\'s best score is {cody_max}')


# Bettina's quiz scores
bettina_quiz_score = quiz_score['Bettina']

# use the function min to determine the lowest score
lowest_score = min(bettina_quiz_score)
# the \'s is used to put 's to words
print(f'Bettina\'s lowest score is {lowest_score}')
