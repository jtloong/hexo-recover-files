---
title: Making PDF-Join
date: 2017/12/22
tags: software-development
---

{% asset_img pdf-join.png %}

My first **real** foray into programming was building web sites and applications for the Ministry of Advanced Education and Skills Development. Before that I had dabbled in VB/VBA scripts/macros and done a few course in Java programming in high school, but I had never truly committed to the art of programming. Building things for the web really opened my eyes to how much fun coding could  be.

And while I still really enjoy web development, my real interest now lies with data science. So with this in mind, I’ve been learning as much as I can in all aspects of the field.

From some of the podcasts and online discussions I consume in my spare time, I’ve become more aware that data science isn’t just about doing research and finding results. In some organizations data science teams are building pipelines and applications that feed data/information to the rest of the business. And one of the favourites for doing this is with the microframework [Flask](http://flask.pocoo.org/).

Flask is a powerful, light-weight web framework and that allows anyone to build web backends / APIs in Python. With the language being a favourite among many data scientists, Flask has become a real asset to many people’s work flow.

Knowing this, I set out to learn my way around the framework and build something with it.

## My Idea

My idea for this web app started with a school project. In my Fall 2017 term at UWaterloo, I took a course called ‘Applied Wetland Science’ where I learned about the science behind building wetlands and the scientific/policy implications surrounding it. In our final paper, my group had to attach two documents together: one of which was a large pdf form. Adobe Acrobat let’s you do this but you need to have the paid edition, and many of the online tools combine way too much functionality or look slightly unscrupulous.

While googling, I stumbled upon this fantastic Python library called [PyPDF2](https://github.com/mstamy2/PyPDF2) which came with all sorts of built in fuctions including the ability to merge pdf documents. With my interest in implementing my new knowledge of Flask, I knew I had to build something.

I needed a dead simple to use, free, non-add web app that did exactly what you needed to do: join multiple pdf documents together. And so I made it.

## Results

Here it is: [http://pdf-join.com](http://pdf-join.com)

It’s a simple site with three routes: an index, an uploader, and a merge/downloader. All the front end is made with a jinja2 templates (which is Flask’s default templating engine) and with custom CSS.

Playing around with Flask’s uploading functionality I made a really barebones version that uploaded and wrote files to a folder in the root directory of the app. However, I figured I might try using an actual database to store all my information for security reasons and honestly just to practice. For this I utilized SQLite which is great to use with Flask and I didn’t need a dedicated server to host the database. On each database insertion I gave a visitor a unqiue ID (written to a cookie), the time of writing, and stored the pdf file as a blob binary.

Using the visitor ID cookie, the merge function could retrieve the users pdf binaries with a simple select statement, using PyPDF2 library to merge it, and sent the written file back to the user. All through Flask!

I used Heroku’s free tier to host it, and after many deploys which managed to crash for varying reasons I got it working!

Overal, I think it really brought together some of my previous work in web development with some of my new data science skills. It was actually a blast to get something like this working, hopefully in my upcoming job I can put these skills to work!
