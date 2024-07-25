import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com/search?q=python+online+compiler&rlz=1C1CHBD_enIN1025IN1025&oq=py&gs_lcrp=EgZjaHJvbWUqEggCEAAYQxiDARixAxiABBiKBTIOCAAQRRgnGDsYgAQYigUyBggBEEUYOTISCAIQABhDGIMBGLEDGIAEGIoFMgYIAxBFGDwyBggEEEUYPDIGCAUQRRg8MgYIBhBFGDwyBggHEEUYPNIBCDUwNjNqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8'
response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.content, 'html.parser')
    
    title = soup.title.string
    print(f"Page Title: {title}\n")
    
    headlines = soup.find_all('h3')
    
    print("Headlines:")
    for idx, headline in enumerate(headlines, start=1):
        print(f"{idx}. {headline.get_text(strip=True)}")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
