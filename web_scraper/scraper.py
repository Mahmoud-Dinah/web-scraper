import requests
from bs4 import BeautifulSoup

requests_url = "https://en.wikipedia.org/wiki/History_of_Mexico"

def get_citations_needed_count(url):
    response = requests.get(url)
    soup=BeautifulSoup(response.text,'html.parser')
    result=soup.find_all('sup',class_ = 'inline-Template')
    return(len(result))

# get_citations_needed_count(requests_url)