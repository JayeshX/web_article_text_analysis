import pandas as pd
import requests
from bs4 import BeautifulSoup

dataframe1 = pd.read_excel('C:/Users/User/Desktop/interndrive/input.xlsx')
blacklist = [
        'pre', 'label', 'html', 'script', 'meta', 'input', 'figcaption', 'style', 'time', 'div', 'ul', 'h1', 'body',
        'li', 'form', '[document]', 'head', 'span', 'a', 'h3'
    ]
for index, row in dataframe1.iterrows():
    url = row['URL']
    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')
    text = soup.find_all(text=True)
    output = ''

    for t in text:
        if t.parent.name not in blacklist:
            output += '{} '.format(t)

    f = open("C:/Users/User/Desktop/git trial/"+str(row['URL_ID'])+".txt", "w",encoding="utf-8")
    f.write(output)
