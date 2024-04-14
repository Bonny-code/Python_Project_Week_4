# here we are creating a list and talking about the positions
# of objects

streets = ['Lake', 'Hennepin', 'Lyndale']
print(streets)
# the print statement here prints the entire list
# the object positions start from 0

print(streets[0])
print(streets[1])
print(streets[2])

# you can add and replace objects into the list using index positions
# if you add an item into an index position longer than the list,
# the program will crash.

streets[1] = 'Frankline'

streets[2] = '1st Avenue'
print(streets)

# using a loop to print individual street names
for street in streets:
    print(street)
# the delivery instructions will ask u for an input
delivery_instructions = 'Please deliver to these streets '

# a for loop is used with a print statement at the end.
for street in streets:
    delivery_instructions = delivery_instructions + street
print(delivery_instructions)
