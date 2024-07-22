from bs4 import BeautifulSoup
import os
import pandas as pd

d = {'title': [], 'price': [], 'link': []}

for file in os.listdir("data"):
    try:    # to escape from those products, which don't give the value
        with open(f"data/{file}") as f:
          html_doc = f.read()
        
        soup = BeautifulSoup(html_doc, 'html.parser')
        
        #print(soup.prettify())
        t = soup.find("h2")
        title = t.get_text()
        
        l = t.find("a")
        link ="https://amazon.in/" + l['href']
        
        p = soup.find("span", attrs={"class": 'a-price-whole'})
        price = p.get_text()
        d['title'].append(title)
        d['price'].append(price)
        d['link'].append(link)

        # print(title , price)
    except Exception as e:
       print(e)

  #break if i want to print only 1 
df = pd.DataFrame(data=d)
df.to_csv("data..csv")