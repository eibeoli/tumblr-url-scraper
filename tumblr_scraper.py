import requests

# This script asks the user to input a list of urls, then goes through them
# and checks availabilty via the status code of the site.
# Note: Make sure you have requests installed; if not, open the command prompt and type
# > pip install requests

url_input = input("Enter urls here, separating them with a comma ',': ")
url_list = []
url_list = url_input.split(", ")

# name of the text file with the stored extensions
filename = 'available_urls.txt'

available = []

for u in url_list:
    r = requests.get(f'http://{u}.tumblr.com')
    if r.status_code == 200:
        print(f'{u} exists')
    elif r.status_code == 404:
        print(f'{u} may be vacant!')
        available.append(u)
    else:
        print(f'{u}: Status Code {r.status_code}')

with open(filename, 'w') as f:
    f.write('Available extensions:\n\n' + '\n'.join(n for n in available))

print(f'Available extensions saved in "{filename}".')
