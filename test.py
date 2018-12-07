import os
from tomd import Tomd
from bs4 import BeautifulSoup
import codecs

path = "posts/Applying-the-Bradford-Hill-Criteria-to-Economics-and-Policy/index.html"

f = codecs.open(path, 'r')
file = f.read()

md = Tomd(file).markdown

with open('test.md', 'w') as file:
    file.write(md)