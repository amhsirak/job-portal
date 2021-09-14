## Description

Job portal is a web application where the candidates can register  and search for suitable jobs and employers can register to post job vacancies at their company. The application provides job catalogue and information which helps the candidates decide which jobs to apply for. 

The 3 user roles are Candidate , Employer and Admin

### Candidate
* Can search for jobs based on different criterias ( Location , Role , Contract )
* Apply for any number of jobs
* View applied jobs in the dashboard

### Employer 
* Can add / update / delete jobs
* Can view job applications ( Only for their jobs )

### Admin
* Can add / remove employers
* Can add / remove any user
* Can add / update / delete jobs
* Can view / delete any job applications 


## Tech Stack

* Django
* Bootstrap 4
* HTML / CSS
* PostgreSQL


## Setup

Clone the repository:

```
git clone https://github.com/karishmashuklaa/job-portal.git
```

Create a virtual environment to install dependencies in and activate it:

```
virtualenv env
```

```
env/Scripts/activate
```

Make migrations: 

```
python manage.py makemigrations
```

```
python manage.py migrate
```

Run the project:

```
python manage.py runserver
```

## Screenshots 

<img width="960" alt="2021-05-18 (13)" src="https://user-images.githubusercontent.com/76456498/119213796-895d5280-badf-11eb-95f7-fa6ebb385b6d.png">

<img width="960" alt="2021-05-18 (7)" src="https://user-images.githubusercontent.com/76456498/119213823-b27de300-badf-11eb-98b6-5e01b6bf5dde.png">

<img width="960" alt="2021-05-18 (8)" src="https://user-images.githubusercontent.com/76456498/119213816-a1cd6d00-badf-11eb-841f-91349e37aadd.png">

<img width="960" alt="2021-05-18 (9)" src="https://user-images.githubusercontent.com/76456498/119213806-99753200-badf-11eb-9625-badf05e4413f.png">


