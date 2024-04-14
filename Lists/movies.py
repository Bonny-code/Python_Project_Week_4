import random

# always import random at the top if u need to use it

movies = ['Spartacus', 'Billions', 'Game_Thrones', 'Black_Sails']

movies.sort()
movies.reverse()

# u can use any variable in the space of movie and it will work
for movie in movies:
    print(movie)

# to add a new movie
movies.append('Assassins')
print(movies)

number_of_movies = len(movies)
print(f'There are {number_of_movies} movies in the list ')

# error to remove something that is not there.
# to remove an item from the list using the remove key word
movies.remove('Blacksails')
print(movies)

# use the pop method if u know the object u wanna remove from the list

last_movie = movies.pop(1)
print(movies)
print(last_movie)

# using random and printing a list
random.shuffle(movies)

# always sorround your variables with curly braces when using f strings
for index, movie in enumerate(movies):
    print(f'{index+1} {movie}')
