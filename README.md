M.bot
===

This repo contains a frame for processing different tasks that you can implement with Python

My idea behind this construction is a possibility to run tasks that satisfy:
* Schedule
* Control
* Statistics
* One task - One python file

So, to archive this I chose architecture with entities:
* Robot _(A DB record, that handle a python file (implemented as python class))_
* Strategy _(That one python file with described task)_

#### Requirements


* Python 3.6+
* Django 2.2+ (Not tested in Django 3+)
* Django Background Tasks 1.2.5+


#### Usage

You can run it locally with standard django server or run it in docker

##### Locally with docker

```
$ cd ./mbot
$ docker-compose up
```

##### Locally with Django development server
```
$ python manage.py runserver
```

After that you can open **m.bot** admin panel with http://127.0.0.1:8000/

#### Contribute
Please, do your work in a fork or in a different branch from the `master` and then submit a PR