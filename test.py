import os
from tomd import Tomd
from bs4 import BeautifulSoup
import codecs

path = "posts/Applying-the-Bradford-Hill-Criteria-to-Economics-and-Policy/index.html"

f = codecs.open(path, 'r')
html = f.read()

soup = BeautifulSoup(html, features="html5lib")

title = "# " + soup.find("h1").get_text().strip()

content = soup.find(itemprop="articleBody")
md = Tomd(str(content)).markdown

with open('test.md', 'w') as file:
    file.write(title + "\n" + md)