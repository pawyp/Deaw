
deaw 
========================================================
aioHTTP made easy

### What is aioHTTP ?
aioHTTP is an HTTP client/server for asyncio. It provides an asynchronous server architecture that provides huge network performance. There are a lot of benchmarks online so I'll let you look up to it. This project wants to make it easier to start-up a project, deploy and structure it.

### What are asynchronous servers ?
One simple way to describe it is that your server is now capable of doing multiple things and the same time.

### Features
- Supports both Server WebSockets and Client WebSockets out-of-the-box.
- Web-server has Middlewares, Signals and pluggable routing.
- Highly scalable
- Lightweight
- HTTP, JSON
- Template rendering with Jinja
- ORM database structure

### Installation
pip3.5 install deaw

### Usage

#### deaw-admin.py

##### startproject
  -  Setup a working directory

> deaw-admin.py startproject projectname

##### startapp
  - Setup an app's working directory

> deaw-admin.py startapp appname

manage.py

>env/bin/python3.5 manage.py to start the server

It runs localy on 127.0.0.1 : 8000

