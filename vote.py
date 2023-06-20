import random
import pyautogui as gui
import time
import requests

def pick_random_name(file_path):
    with open(file_path, 'r') as file:
        names = file.readlines()
    random_name = random.choice(names).strip()  # Remove leading/trailing white spaces and newlines
    return random_name

def load_proxies_from_file(file_path):
    proxies = []
    with open(file_path, 'r') as file:
        for line in file:
            proxy = line.strip()  # Remove leading/trailing white spaces and newlines
            proxies.append(proxy)
    return proxies

def make_request_with_proxies(url, proxies):
    for proxy in proxies:
        try:
            response = requests.get(url, proxies={'http': proxy, 'https': proxy}, timeout=5)
            return response
        except requests.exceptions.RequestException:
            continue
    return None

names_file = 'names.txt'
random_name = pick_random_name(names_file)

proxy_file = 'proxies.txt'
proxies = load_proxies_from_file(proxy_file)

# Replace "https://minecraft-mp.com/server/318753" with the actual URL you want to request
url = "https://minecraft-mp.com/server/318753/vote/"
response = make_request_with_proxies(url, proxies)

time.sleep(1)

user = "user.png"
captcha = "captcha.png"
vote = "votebutt.png"
gui.click(user)
gui.typewrite(random_name)
gui.click(captcha)
gui.click(vote)




