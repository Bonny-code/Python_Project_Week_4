import openpyxl

workbook = openpyxl.load_workbook('ITEC_Courses.xlsx')

# this is to make sure e are working with the correct sheets

sheet_names = workbook.sheet_names
# the names of the sheets will be printed.
print(sheet_names)

# to select which sheet we are working with
codes_sheet = workbook.active

# to get data from a cell
b2_data = codes_sheet['B2'].value
print(b2_data)

# TRYING FOR OTHER CELLS
c5_data = codes_sheet['C5'].value
print(c5_data)

# to print an entire row in the spreadsheet
for row in codes_sheet.row:
    # to print cell in row
    for cell in row:
        print(cell.value)
print()

# get all data from first and secind column
for col in codes_sheet.columns:
    for cell in col:
        print(cell.value)
print()

# get all data from one column
class_names_column = codes_sheet['B']
for cell in class_names_column:
    print(cell.value)

# get another sheet, by name
rooms_sheet = workbook['rooms']
rooms_column = rooms_sheet['B']
for cell in rooms_column:
    print(cell.value)

