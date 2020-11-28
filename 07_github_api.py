import requests 

#CONSTANTS
BASE_URL = 'https://api.github.com/'
response = requests.get(BASE_URL)
print(response.status_code)


#username = input('Give me a github username:\t')