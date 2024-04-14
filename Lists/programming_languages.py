# you must import random to use it or shuffle
import random

languages = ['Python', 'Java', 'Javascript', 'C', 'Swift']

for language in languages:
    print(language)

# to join langueges u use the .join
all_languages = ''.join(languages)
print(all_languages)

# to sort out the langauges u use the .sort
languages.sort()
print(languages)

# to reverse languages u use the .reverse
languages.reverse()
print(languages)

# to add a new language
languages.append('Kotlin')
print(languages)

# by default pop will remove the last item on the list
# remove will remove the said item from the list
languages.remove('Swift')

# here we use the + operator to combine two lists
alice_languages = ['Java', 'Javascript', 'C',]
bob_languages = ['Python', 'Swift']
team_languages = alice_languages + bob_languages
print(team_languages)

# using the sort parameter
team_languages.sort()
print(team_languages)

# using the random and shuffle to mix things up
random.shuffle(team_languages)
print(team_languages)