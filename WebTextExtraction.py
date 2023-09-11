import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()

input_file_path = os.getenv('input_excel')
extoutputpath = os.getenv('Extract_output')

dataframe1 = pd.read_excel(input_file_path)
blacklist = [
        'pre', 'label', 'html', 'script', 'meta', 'input', 'figcaption', 'style', 'time', 'div', 'ul', 'h1', 'body',
        'li', 'form', '[document]', 'head', 'span', 'a', 'h3'
    ]

for index, row in dataframe1.iterrows():
    print(index)
    url = row['URL']
    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')
    text = soup.find_all(string=True)
    output = ''

    for t in text:
        if t.parent.name not in blacklist:
            output += '{} '.format(t)

    f = open(extoutputpath+str(row['URL_ID'])+".txt", "w",encoding="utf-8")
    f.write(output)
