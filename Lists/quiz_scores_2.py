# here we are printing quiz scores

quiz_scores = [0] * 5
print(quiz_scores)

# using the range parameter in a loop
for quiz in range(5):
    score = int(input(f'Enter score for {quiz + 1} '))
    quiz_scores[quiz] = score

# the results are printed here
print('Your score are ')
print(quiz_scores)
