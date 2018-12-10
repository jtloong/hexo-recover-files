# Hexo-recover-files

Recover your markdown files from your static repository for your Hexo based site.

For those (like me) who were silly and did not back up their precompiled markdown files for their Hexo blog, hopefully this repo helps. The goal is to be able to clone your static repo with your compiled HTML files to  convert them back into markdown and the proper pre-compiled directory structure.

This project requires Python 3. 

## Supported Features

This project can rebuild the following features:

* Directory structure found in your `source/_posts` 
* YAML front-matter (only title, date, and tags supported)
* Headers (h1, h2, h3 etc.)
* Images and their assets
* Iframes

## Instructions

1. Install the repo

	```bash
	git clone https://github.com/jtloong/hexo-recover-files
	cd hexo-recover-files
	pip install -r requirements.txt
	```

2. Clone your static website repo with your compiled files

3. Edit the `locations.json` file with the folder locations of your static repo:
	* Change `static_folder` value to the name of your repo
	* Change `post_folder` array to the locations of your post folders

4. Run `python extract.py`

The extraction script will build a `posts/` directory with all of your pre-compiled markdown files and their assets.

## Notes

I've only so far tested this on my static repo and it mostly works. Let me know if you run into any issues!

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details