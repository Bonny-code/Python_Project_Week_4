# creating a dictionary of movie ratings

movie_ratings = {'Spartacus': 8, 'Blacksails': 7, 'Billions': 9, 'Suits': 5, 'Top Tarzan': 10}

print(movie_ratings)

# printing a movie rating

billions_ratings = movie_ratings['Billions']
print(billions_ratings)

# change movie ratings
movie_ratings['Spartacus'] = 9
print(movie_ratings)

# rating for a movie that doesnt exist
# it will print none if there is no value
batman_ratings = movie_ratings.get('Spartacus')
print(batman_ratings)

# check if there is no rating for a movie
if batman_ratings is None:
    print('There is no rating for the movie selected.')
else:
    # this below will be printed if there is a rating
    print('There is a rating and it is ' + str(batman_ratings))

suit_ratings = movie_ratings.get('Suits')
print(suit_ratings)

if 'Suits' in movie_ratings:
    print('Suits is one of the movies rated')
else:
    print('Suits is Not one of the movies rated.')

if 'Inside out' in movie_ratings:
    print('Suits is one of the movies rated')
else:
    print('Suits is Not one of the movies rated.')


# adding data to the dictionary
movie_ratings['24'] = 10
print(movie_ratings)

# writing a loop to print things in the dictionary to print keys
for movie_name in movie_ratings:
    print(movie_name)

# using the .items to loop over keys and values
for movie_name, rating in movie_ratings.items():
    print(f'{movie_name} has a rating of {rating} out of 10')


# Removing items from dictionary with pop
print(movie_ratings)
batman_ratings = movie_ratings.pop('24')
print(movie_ratings)
# this will print the value of the movie that is popped.
print(batman_ratings)

# to remove something that is not on the list
if 'Avenger' in movie_ratings:
    movie_ratings.pop('Avengers')
# if the value to be removed is not there, then it will just
# print the list all over again
print(movie_ratings)



