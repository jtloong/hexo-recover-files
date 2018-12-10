---
title: Getting Started With Local Open edX Development
date: 2018/03/22
tags: software-development
---

{% asset_img classroom.jpg %}

The world of online learning is vast. There are a myriad of options available for the prospective client wishing to distribute training/education. Many of them paid, some of them free, all of them have their strengths and weaknesses.

As part of my work at [Democracy Kit](https://democracykit.org), where I am the tech lead, we’ve begun to dive head first into the crazy realm of MOOC’s. After discussing it we’ve decided, at least for now, to build out a prototype of what a Democracy Kit branded online course platform would look like.

The current website that we use is great for what we’ve needed for our first year in operation, but now we’re exploring options that give us a bit more flexibility.

And the platform we’ve chosen to do that is [Open edX](https://open.edx.org/), a completely open source version of the MOOC software that runs [edX](https://www.edx.org/). Open edX is built mostly in Django with a MongoDB and MySQL backend, utilizing Django templates and SASS for the frontend.

## Going Local

So a few weeks ago we tried our hand at using it, and before we had even written a single line of code we came at a roadblock.

The current documentation for setting up a local development environment is a bit confusing. They initially recommend setting up their local dev version of the software using Vagrant and Virtual Box. Both [Hasan](https://twitter.com/HasanNaseem) and I tried it on our computers (one Mac and one Linux machine), and we both ran into huge problems.

Error after error; all sorts of problems. And not a single line of code had been written yet. Just setting up a dev environment seemed like it was more difficult than we expected.

It turns out Open edX is currently making a transition from their old local development deployment and using Docker containers. After scratching our heads for a little bit, we found [this repo](https://github.com/edx/devstack) outlining a much more sane way to getting started.

But even this documentation was confusing, which is why I’m writing this blog post to help teach anyone who wants to start developing with us or to random visitors to my little corner of the web that need help deploying their first Open edX app.

## Installing Open edX: a (Dummy’s) Survival Guide

1. Install [docker-compose](https://docs.docker.com/compose/install/)
1. Make sure you have **make** and **pip** installed
1. Install [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/#lower-level-virtualenv)
<li>Clone this repository using:
<figure class="highlight zsh"><table><tbody><td class="gutter"><pre>1<br/></pre></td><td class="code"><pre>git clone https://github.com/democracykit/devstack.git<br/></pre></td>
</tbody></table></figure>
</li>
<li>Move into the project folder and create a virtualenv using:
<figure class="highlight zsh"><table><tbody><td class="gutter"><pre>1<br/>2<br/></pre></td><td class="code"><pre>cd devstack<br/>virtualenv democracykit<br/></pre></td>
</tbody></table></figure>
</li>
<li>Then install requirements like so:
<figure class="highlight zsh"><table><tbody><td class="gutter"><pre>1<br/></pre></td><td class="code"><pre>make requirements<br/></pre></td>
</tbody></table></figure>
</li>
<li>The Docker Compose file mounts a host volume for each service’s executing code by conducting this command:
<figure class="highlight zsh"><table><tbody><td class="gutter"><pre>1<br/></pre></td><td class="code"><pre>make dev.clone<br/></pre></td>
</tbody></table></figure>
</li>
<li>Run the provision command to configure the superusers which may take a while (my installation took almost half an hour):
<figure class="highlight zsh"><table><tbody><td class="gutter"><pre>1<br/></pre></td><td class="code"><pre>make dev.provision<br/></pre></td>
</tbody></table></figure>
</li>
<li>Start the services (this may take up to 60 seconds to appear even after all the checks say done):
<figure class="highlight zsh"><table><tbody><td class="gutter"><pre>1<br/></pre></td><td class="code"><pre>make dev.up<br/></pre></td>
</tbody></table></figure>
</li>

And voila! You should have a version of Open EdX devstack running on your local machine. All of the services are running at the following links:

|Service|URL
|------
|Credentials|[http://localhost:18150/api/v2/](http://localhost:18150/api/v2/)
|Catalog/Discovery|[http://localhost:18381/api-docs/](http://localhost:18381/api-docs/)
|E-Commerce/Otto|[http://localhost:18130/dashboard/](http://localhost:18130/dashboard/)
|LMS|[http://localhost:18000/](http://localhost:18000/)
|Studio/CMS|[http://localhost:18010/](http://localhost:18010/)

Once you’re done with working for the day you can stop the services using:<br/>

``` plain
make stop
```


## Actually Developing

Now you’ve installed a wackload of code and files, and set up your databases. Now to actually develop the frontend you have to navigate this tree of folders.

Just a tip, all of your frontend code that students will see is under the `edx-platform/lms` folder. What we’re doing is we’ve setup [a seperate repo](https://github.com/democracykit/open-edx-frontend) that will contain all of our code in this folder. That we can then push and pull code from.

## That’s It!

I hope this helps simplify your understanding of how to launch your own local environment for Open edX development. I know it seems super confusing and daunting at first, and I hope this helps out anyone who wants to help out on the project or wants to develop their own courses.

Thanks for reading!
