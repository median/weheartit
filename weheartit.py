from bs4 import BeautifulSoup
import requests

def look_up(user):
    res = requests.get(f'https://weheartit.com/{str(user)}').text
    soup = BeautifulSoup(res, "html.parser")
    tags = soup.find_all('h1', class_='h1 no-margin text-overflow')

    results = []
    for result in tags:
        results.append(result)
    
    if not results:
        print(f'The username {user} is available!')

with open('list.txt', 'r') as file:
    for user in file:
        look_up(user.strip())
