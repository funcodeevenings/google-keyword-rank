import requests
from bs4 import BeautifulSoup
from collections import OrderedDict

keyword = "hello"
website = 'hello.processing.org'


print("keyword = ",keyword)
print("website = ",website)


length=0
for j in range(0,190,10):
    lis = []
    payload = {'q': keyword, 'start': j}
    r = requests.get('https://www.google.com/search', params=payload)


    soup = BeautifulSoup(r.text, 'html.parser')
    divs = soup.find_all("div", class_="kCrYT")
    for i,div in enumerate(divs):
        # print("i =",i)
        if div.a:
            val = div.a['href']
            x = val.split('/')
            if len(x)>3:
                lis.append(x[3])

    try:
        rank = lis.index(website)
        if rank:
            print("=======PAGE =========",j/10+1)
            print("=======RANK =========",rank+length+1)
            break;
    except:
        length = length+len(lis)
