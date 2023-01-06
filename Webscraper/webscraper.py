import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv = Service('C:/Users/anwar/Downloads/chromedriver_win32/chromedriver.exe')

driver = webdriver.Chrome(service=serv)
driver.get('https://oxylab.io/blog')
results = []
other_results = []
content = driver.page_source
soup = BeautifulSoup(content)

for a in soup.findAll(attrs='css-1kfmdo4 emlf3670'):
    name = a.find('p')
    if name not in results:
        results.append(name.text)

for b in soup.findAll(attrs='css-1kfmdo4 emlf3670'):
    head = b.find('h5')
    if head not in results:
        other_results.append(head.text)

df = pd.DataFrame({'Name': results, 'Head': other_results})
df.to_csv('name.csv', index=False, encoding='utf-8')
