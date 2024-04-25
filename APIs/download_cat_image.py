import requests

# we are adding different urls and to create a list of urls
kitten_picture_urls = ['https://loremflickr.com/cache/resized/65535_53052783191_41d04914e2_320_240_nofilter.jpg',
                       'https://loremflickr.com/cache/resized/65535_53052783191_41d04914e2_320_240_nofilter.jpg'
                       'https://loremflickr.com/cache/resized/65535_53052783191_41d04914e2_320_240_nofilter.jpg']

for index, url in enumerate(kitten_picture_urls):
    response = requests.get(url)
    # below is a loop inside a loop.the with will open the file
    # it will alternate and download different pictures since we have multiple urls
    filename = f'kitten_{index}.jpg'
    # the index keyword will generate a unique file number
    with open(filename, 'wb') as file:
        # the .ter keyword is used to iterate content.
        # so u get to see different pictures from the urls above.
        for chunk in response.iter_content():
            file.write(chunk)
