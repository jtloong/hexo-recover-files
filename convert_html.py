import os
from tomd import Tomd
from bs4 import BeautifulSoup
import codecs
import re


def build_file(name):
    path = "posts/" + name + "/index.html"

    # Added "encoding" parameter, else it would return null
    f = codecs.open(path, "r", encoding="utf-8")

    html = f.read()

    soup = BeautifulSoup(html, features="html5lib")

    # Save title
    md = "---"
    md += "\ntitle: " + soup.find("h1").get_text().strip()
    md += "\ndate: " + soup.find("time").get_text().replace("-", "/")

    # This line caused me some trouble, because in my html files
    # the tags were not displayed.
    #  md += "\ntags: " + soup.find("a", "tag-link").get_text()

    md += "\n---\n"

    content = soup.find(itemprop="articleBody")

    for child in content.children:
        if str(child)[:4] == "<img":
            end_point = child["src"].rfind("/") + 1
            file_name = child["src"][end_point:]
            text = "{% asset_img " + file_name + " %}"
            md += "\n" + text + "\n"
        elif str(child)[:2] == "<h":
            num_pounds = "#" * int(str(child)[2])
            md += "\n" + num_pounds + " " + child.get_text() + "\n"
        elif str(child)[:3] == "<if":
            md += "\n" + str(child) + "\n"
        elif str(child)[:24] == '<figure class="highlight':
            code_sample = str(child)

            code_type = code_sample[25 : code_sample.find('"', 24)]

            temp_md = Tomd(str(child)).markdown
            temp_md = temp_md[temp_md.find('<td class="code"') :]
            temp_md = BeautifulSoup(temp_md, features="html5lib").find("pre")

            pre_md = str(temp_md)
            pre_md = pre_md[5:-6]

            temp_md = "\n``` "
            temp_md += code_type + "\n"
            for i, char in enumerate(pre_md):
                if pre_md[i : i + 5] == "<br/>":
                    temp_md += "\n"
                    temp_md += char
                else:
                    temp_md += char
            temp_md += "```"

            md += temp_md.replace("<br/>", "")
        else:
            md += Tomd(str(child)).markdown

    # Added "encoding" parameter, else it would throw a UnicodeEncodeError.
    with open("posts/" + name + ".md", "w", encoding="utf-8") as file:
        file.write(md)

