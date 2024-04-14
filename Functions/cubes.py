# this function prints number up till 10
# using the range character.

def main():
    for number in range(10):
        c = cube(number)
        print(c)


def cube(value):
    cube_value = value * value * value
    return cube_value

# value is multiplied here 3x to gt cube value


main()
