import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com/'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    paragraphs = soup.find_all('p')
    
    for para in paragraphs:
        print(para.get_text())
        
else:
    print(f"Oops! Couldn't get the webpage. Error code: {response.status_code}")
    print("Try checking the URL or your internet connection.")
    