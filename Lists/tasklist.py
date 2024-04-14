# saving the items in an empty variable

todo_list = []


# the break parameter will be used here to break out of the loop if the
# conditions are not met
while True:
    task = input('Enter your task or press enter to stop. ')
    if task:
        todo_list.append(task)
    else:
        break

print('Thank you, your tasks are ')

# using the index parameter to know the positions of the obejects
# in the list and the enumerate to number them accordingly
for index, task in enumerate(todo_list):
    print(f'task {index + 1} is {task}')

# print(todo_list)
for task in todo_list:
    print(task)

# the len parameter is used to count the number of items in the list
number_of_tasks = len(todo_list)
print(f'ypu have {number_of_tasks} to do. ')