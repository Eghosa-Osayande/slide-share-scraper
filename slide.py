import requests as r
from bs4 import BeautifulSoup as bs

url='https://www.slideshare.net/kamal6902/sonar-40159485'
res= r.get(url)

b1= bs(res.text,features='html.parser')
t=b1.find_all('img',class_='slide-image')
for tt in t:

    attrs=tt.attrs
    # print(f"{attrs.get('data-index')}\n")
    # print(f"{attrs.get('alt')}\n")
    print(f"{attrs.get('src')}\n")
    f=attrs.get('srcset')
    f=f.split(', ')[-1].split(' ')[0]
    # print(f)

    with open(f"slide/{attrs.get('data-index')}.png",'wb') as fd:
        print(attrs.get('data-index'))
        y=r.get(f)
        fd.write(y.content)
    



