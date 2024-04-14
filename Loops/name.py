# in this assignment, i used the variable name to save the users name
# then i used a for loop to print the letters in the name.
# i used the .upper word to convert the letters into upper cases when spelling vertically.
# I used another print statement at the end to thank the user and the users name
# is spelled in the original format.

name = input('Please Enter your name: ')

for letter in name:
    print(letter.upper())

print('That was your name vertically, ' + name + '. Thanks for using this program')
