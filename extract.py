import os
import shutil
import json
import convert_html
from bs4 import BeautifulSoup


def find_path(name, path):
    for root, dirs, files in os.walk(path):
        if name in dirs:
            return os.path.join(root, name)


def get_post_folders(post_parent_folders, static_folder):
    folder_names = []
    folder_paths = []

    for directory in post_parent_folders:
        walk_results = [
            x[1] for x in os.walk(static_folder + "\\" + directory) if x[1] != []
        ]
        folder_names.extend([s[0] for s in walk_results if not s[0].isdigit()])
        folder_paths.extend(
            [
                find_path(s[0], static_folder + "\\" + directory)
                for s in walk_results
                if not s[0].isdigit()
            ]
        )

    return folder_paths, folder_names


# year_folders = [item for item in os.listdir("website/") if item[:2] == '20']

with open("locations.json") as json_data:
    d = json.load(json_data)
    static_folder = d["static_folder"]
    post_parent_folders = d["post_folders"]

# Traverse directories two levels down
folder_paths, folder_names = get_post_folders(post_parent_folders, static_folder)

if os.path.exists("posts\\"):
    shutil.rmtree("posts\\")

if not os.path.exists("posts\\"):
    os.mkdir("posts\\")

for index, folder in enumerate(folder_paths):
    try:
        shutil.copytree(folder, "posts\\" + folder_names[index])
    except:
        print("Folder already copied.")

for post in folder_names:
    try:
        convert_html.build_file(post)
        print("Built " + post)
        os.remove("posts/" + post + "/index.html")
    except:
        print("No file")
