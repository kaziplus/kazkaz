## KazKaz

---
Duma job matching challenge.

---
Design and build a job matching system MVP
It should be able to match a job to job seekers based on relevant variables.

Required features:
- Post a job and define which variables (decided by you) are mandatory and which are optional
- Match that job to a defined number of job seekers based on relevant variables

Optional features:
- Send messages (sms/email) to selected job seekers with a customised message telling them how to report their interest in the job
- Remove unwanted job seekers from the list
- Save the job match to be able to go back to it later

Other requirements:
- The application should be written in Django
- Please deploy the application to an environment where you can demo it to us
- Please create a github repo where you will commit the code so that you can show it to us

---

### Overview

---
This is a [Django](https://www.djangoproject.com/) power web application.

The main building blocks are:

* [Django](https://www.djangoproject.com/)
* [Postgres](http://www.postgresql.org/)

### Structure

---
![Tree](https://github.com/mattgathu/kazkaz/raw/master/tree.jpeg)

kazkaz has been built more or less as a traditional / conventional Django project
with only a few changes:

* local applications have been grouped under the `apps` folder
* all configs reside in the `config` folder


### Demo

---

The application is running on Heroku, you can view it [Here](https://kazkaz.herokuapp.com/).


### Contributors

---
The project is wholly written by [Matt Gathu](http://mattgathu.me)
