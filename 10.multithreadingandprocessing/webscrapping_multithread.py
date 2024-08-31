
'''
https://python.langchain.com/v0.2/docs/introduction/
https://python.langchain.com/v0.2/docs/concepts/
https://python.langchain.com/v0.2/docs/tutorials/

'''

import threading
import requests
from bs4 import BeautifulSoup

urls = [
    'https://python.langchain.com/v0.2/docs/introduction/',
    'https://python.langchain.com/v0.2/docs/concepts/',
    'https://python.langchain.com/v0.2/docs/tutorials/'
]

def fetch_contents(urls):
    response = requests.get(urls)
    soup = BeautifulSoup(response.content,'html.parser')
    print(f'Fetched {(soup.text)} characters from {urls}')

threads =[]
for url in urls:
    thread = threading.Thread(target=fetch_contents,args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All web pages fetched")