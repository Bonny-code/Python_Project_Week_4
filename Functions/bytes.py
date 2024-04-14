# here we are converting megabytes to bytes
# make sure you name your functions and variables correctly
# the mai function is called first irrespective of its position

def megabytes_to_bytes(megabytes):
    bytes = megabytes * 1000000
    return bytes


def main():
    b = megabytes_to_bytes(10)
    print(b)


main()
