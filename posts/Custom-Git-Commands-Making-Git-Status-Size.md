---
title: Custom Git Commands: Making Git-Status-Size
date: 2018/10/22
tags: software-development
---

{% asset_img example.gif %}

Sometimes you find a task that seriously disrupts your workflow and so you have to make something to fix it.

That was the biggest reason why I made [git-status-size](https://github.com/jtloong/git-status-size). Too many times I would not pay attention to things I would add/commit/push and end up messing up my whole working tree with an accidentally committed large file. This would mean a whole lot of wasted time reverting back to a previous commit.

So I created git-status-size, which is a simple custom git utility that allows me to see the file sizes of all my untracked, uncommitted or changed files in my repo.

It’s incredibly simple. You can follow the instructions on the repo (I’ve linked above), and once installed you can do a simple call `git status-size` in any of your git repos and get an output similar to what you can see in the gif above.

Each line has a type of change (with a different colour for each), the file name, and size. This way I could easily double check I’m not breaking anything before I push to Github.

## Do you have your own problem you need to solve?

I actually haven’t done too much bash scripting before, but after doing this mini-project I think it’s extremely useful to learn how to make your own custom commands. This is especially apparent when interacting with software where you have to repeat a lot of commands in the terminal (like git).

So how do you do you make your own custom git command? It’s actually incredibly easy:

<li>Write a bash script to accomplish a repetitive or annoying task. You can use [mine for reference](https://github.com/jtloong/git-status-size/blob/master/git-status-size) and title it something like `git-do-annoying-task`.
</li>
<li>To invoke it anywhere you’ll need to export the file into your PATH. In your script file use `export PATH="/path/to/your-script/directory:$PATH`<sup>1</sup>.
</li>
<li>Once the script is moved, you’ll need to make it executable. You can just move into that folder and execute `chmod +x git-do-annoying-task`.
</li>
<li>Now try it out! Move to any repo you have on your machine and try `git do-annoying-task` and voila! you have your own custom git command.
</li>

Now this principle also applies if you want to simplify any type of workflow on your computer, not just git. I just wanted to use git because its such a common thing many developers have to work with.

## Thanks for reading!

Thanks for reading this mini-blog post. I hope this helps anyone that has had an issue with git or some other terminal process that you need to simplify.

Give me a shoutout if you have any questions/thoughts/concerns on Twitter [@jtloong](https://twitter.com/jtloong) or at [joshua.t.loong@gmail.com](mailto:joshua.t.loong@gmail.com)

The command line output gif was made with [terminalizer](https://github.com/faressoft/terminalizer).

## Notes

<sup>1. Thanks to /u/alfunx on Reddit for pointing out an error in the first version of the post.</sup>
