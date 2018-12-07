import os
from tomd import Tomd
from bs4 import BeautifulSoup
import codecs


def build_file(name):
	path = "posts/" + name + "/index.html"

	f = codecs.open(path, 'r')
	html = f.read()

	soup = BeautifulSoup(html, features="html5lib")

	# Save title
	md = "title: " + soup.find("h1").get_text().strip()
	md += "\ndate: " +  soup.find("time").get_text().replace("-", "/")
	md += "\ntags: " + soup.find("a", "tag-link").get_text()
	md += "\n---\n"

	content = soup.find(itemprop="articleBody")

	for child in content.children:
		if str(child)[:4] == '<img':
			end_point = child['src'].rfind('/') + 1
			file_name = child['src'][end_point:]
			text = "{% " + file_name + " %}"
			md += "\n" + text + "\n"
		elif str(child)[:2] == '<h':
			num_pounds = "#" * int(str(child)[2])
			md += "\n" + num_pounds + " " + child.get_text() + "\n"
		elif str(child)[:3] == '<if':
			md += "\n" + str(child) + "\n"
		else:
			md += Tomd(str(child)).markdown

	with open('posts/' + name + '.md', 'w') as file:
	    file.write(md)