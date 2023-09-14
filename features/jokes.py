import requests

def tell_a_joke():
    data = requests.request("GET", "https://v2.jokeapi.dev/joke/Any")
    joke = data.json()
    if joke['type'] == 'single':
        joke = joke['joke']
    else:
        joke = joke['setup'] + ' ' + joke['delivery']
    return joke