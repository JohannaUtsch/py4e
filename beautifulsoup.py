import urllib.request,urllib.parse
from bs4 import BeautifulSoup

url = input('Enter - ')

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,"html.parser")
tag = soup("span")
count=0
sum=0
for i in tag:
 x=int(i.text)
 count+=1
 sum = sum + x

print(count)
print(sum)
