def main():
    length = int(input('Enter length: '))
    width = int(input('Enter width: '))
    height = int(input('Enter height: '))
    calculate_volume(length, width, height)

# use descriptive variable names
# with the volume you multiply all the paramters


def calculate_volume(length, width, height):
    # the necessary data is supplied as parameters
    volume = length * width * height
    print(f'the volume of tge box is {volume}')


main()
