import urllib.request, urllib.parse, urllib.error, bs4
x = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
print(x)

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
x = soup('a')