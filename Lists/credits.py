# lit is used to hold different numbers

credits_per_class = [4, 3, 3, 2]

# an empty variable is used to hold the total
total = 0

# a for loop is used here and the total is printed below
for credit_count in credits_per_class:
    total = credit_count + total
    print(f'{credit_count}, total so far {total}')

print(total)

# the sum parameter is used here and the total is printed
total_with_sum_function = sum(credits_per_class)
print(total_with_sum_function)

# an if or else statement describing to check if the
# student is full time or part time or not
# eligible at all if the credits are less than 6
if total >= 12:
    print('You are a full time student. ')
elif total >= 6:
    print('You are a part time student. ')
else:
    print('You are less than a part time student. ')