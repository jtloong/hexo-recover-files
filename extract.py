import os
import shutil
from bs4 import BeautifulSoup


def find_path(name, path):
    for root, dirs, files in os.walk(path):
        if name in dirs:
            return os.path.join(root, name)

def get_post_folders(year_folders):
	folder_names = []
	folder_paths = []

	for year in year_folders:
		walk_results = [x[1] for x in os.walk("website\\" + year) if x[1] != []]
		folder_names.extend([s[0] for s in walk_results if not s[0].isdigit()])
		folder_paths.extend([find_path(s[0], "website\\" + year) for s in walk_results if not s[0].isdigit()])


	return folder_paths, folder_names

year_folders = [item for item in os.listdir("website/") if item[:2] == '20']

# Traverse directories two levels down
folder_paths, folder_names  = get_post_folders(year_folders)
print(folder_paths)

if not os.path.exists('posts\\'):
	os.mkdir('posts\\')

for index, folder in enumerate(folder_paths):
	try:
		shutil.copytree(folder, 'posts\\' + folder_names[index])
	except:
		print('Folder already copied.')

