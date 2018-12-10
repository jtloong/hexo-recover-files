---
title: Improving My Hexo Blogging Workflow
date: 2018/07/30
tags: software-development
---

{% asset_img hexo.png %}

[Hexo](https://hexo.io/) is a simple static site web framework built using Node.js (similar to other famous blogging frameworks such as Jekyll and Hugo). I’ve been using it for this blog and I’ve really liked using it.

I used to use Wordpress for a book review blog I had, but decided to move away from it mostly because:

1. Theming on Wordpress is a bigger mess than its worth
1. Wordpress can be super slow sometimes, static site frameworks are light-weight
1. With Hexo I own everything end-to-end

Despite my love for Hexo, there’s a few things that have bothered me about the workflow. So I wrote some simple scripts to make my work easier and I thought I’d share:

## Deleting published posts

Most of Hexo is controlled using terminal commands. You can create drafts, publish posts, deploy your site etc. A full list of the commands can be found [here](https://hexo.io/docs/commands).

But what always frustrated me was that there was no explicit command to delete a post once it’s been published. I expect it’s so you can’t easily delete something you wanted to keep live. Either way, I created a tiny bash script so that you can do that.

[I’ve uploaded it to Gist](https://gist.github.com/jtloong/60d4449eb45e0c7104264f082cf75058) but you can see the script here:

``` bash
#!/bin/bash
POST_DIR=source/_posts/

rm $POST_DIR$1.md
rmdir $POST_DIR$1/
hexo clean
hexo generate
```
All you need to do it is put it in the root of your Hexo project and call the command `bash hexo_delete_post.sh file_name` where file_name is without the file extension (ie .md)

## Moving published post back to drafts

One thing I always like to do is visualize what my post is going to look like when it’s live on the site. Good thing with Hexo is that you can generate and serve your blog locally to see it before it goes live.

BUT the only way to do that is to publish your draft. All changes will remain local until its deployed to your live site, but sometimes I want to work on a post, look at it, and then stash it away.

So I wrote the following script to move published posts back to drafts. The Gist can be found [here](https://gist.github.com/jtloong/fe74c26f0efc5be7d407ef78d34c7609).

``` bash
#!/bin/bash
POST_DIR=source/_posts/
DRAFT_DIR=source/_drafts/

mv $POST_DIR$1.md $DRAFT_DIR
mv $POST_DIR$1/ $DRAFT_DIR
hexo clean
hexo generate
```
The instructions are the same as the last script: put this in the root of your Hexo project and call the command `bash move_to_draft.sh file_name` where file_name is without the file extension (ie .md)

## Thanks for reading!

Hope that helps you fellow Hexo users out there. I know this is relatively simple stuff but it might help someone so I figured I’d write about it.

Since Hexo is open source I might eventually get around to contributing some functions to make this built in. But until I have time, this will have to do for now.
