import docx
# always import docx like the other libraries


# here we are importing the text document we downloaded
document = docx.Document('IT_Sample_Resume.docx')

# to print the paragraphs from the Word documents.
# use this code to search for specific words in a document
# u can replace the highlighted word with what u want.
for para in document.paragraphs:
    # to replace specific words in the paragraph
    if 'ethical hacker' in para.text.lower():
        print('An ethical hacker')
    # print(para.text)

