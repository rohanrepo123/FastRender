from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
app = FastAPI()

@app.get('/')
def home():
    return {'message':'Hello From Fastapi'}

@app.get('/about')
def about():
    return {'message':'About Page'}


@app.get('/news')
def news(page:int=1, limit:int=5):
    url = 'https://www.thehindu.com/' 
    url2 = 'https://indianexpress.com/'
    response = requests.get(url2)
    clean_text = BeautifulSoup(response.text,'html.parser')
    start = (page -1 )*limit
    end = start + limit
    title = []
    # for i in clean_text.find_all('a',class_='topblockNews__sidebarLink'):
    for i in clean_text.find_all('h4',class_='o-commonList__txt'):
        title.append(i.text)
    
    return {"page":page,'news':title[start:end],"limit":limit,'no. of news':len(title)}
