
history = []

# visiting example pages

history.append('www.google.com')
history.append('www.minneapolis.edu')
history.append('www.stackoverflow.com')

# pressing the back button deletest the pages.
print(history.pop())
print(history.pop())
print(history.pop())

print(history)