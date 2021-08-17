import requests
from bs4 import BeautifulSoup

requests_url = "https://en.wikipedia.org/wiki/History_of_Mexico"

def get_citations_needed_count(url):
    response = requests.get(url)
    soup=BeautifulSoup(response.text,'html.parser')
    result=soup.find_all(class_ = 'Inline-Template')
    return(len(result))

# get_citations_needed_count(requests_url)

def get_citations_needed_report(url):
    response = requests.get(url)
    soup=BeautifulSoup(response.text,'html.parser')
    result=soup.find_all(class_ = 'Inline-Template' )
    paragraph_contain_citation = []

    for p in result:
        paragraph_contain_citation.append(p.parent.text.strip())
    return '\n'.join(paragraph_contain_citation)



if __name__=='__main__':

    print(get_citations_needed_report(requests_url))
    print(get_citations_needed_count(requests_url))