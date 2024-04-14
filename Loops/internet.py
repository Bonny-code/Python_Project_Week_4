from urllib import request  # used to connect to internet resources
from time import sleep   # this will pause the program for a while

# we hve to use  url from a website that is
# expected to be available all the tme
url = 'https://www.google.com'

seconds_to_sleep_between_checks = 3

while True:
    print('Checking if you are online')
    try:
        # try to open the url and it will fail if you are not online
        request.urlopen(url).read()
        print('You seem to be online')
    except:  # this section will run if yu cant connect to the url
        print('You are not online')
    print(f'sleeping for {seconds_to_sleep_between_checks} seconds ...')
    print()
    sleep(seconds_to_sleep_between_checks)
# use f strings instead of concactenations.