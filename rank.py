import requests
from bs4 import BeautifulSoup
from collections import OrderedDict

keyword = "puma"
website = 'www.amazon.in'


print("keyword = ",keyword)
print("website = ",website)

payload = {'q': keyword}
r = requests.get('https://www.google.com/search', params=payload)

# print("url =",r.url)

# print("response =",r.text)

soup = BeautifulSoup(r.text, 'html.parser')
divs = soup.find_all("div", class_="kCrYT")
# print(soup.prettify())

# print(soup.cite)

lis = []
for i,div in enumerate(divs):
    # print("i =",i)
    if div.a:
        val = div.a['href']
        x = val.split('/')
        if len(x)>3:
            lis.append(x[3])


ans = list(OrderedDict.fromkeys(lis))

# print(ans)


rank = ans.index(website)
print("=======RANK =========",rank+1)
