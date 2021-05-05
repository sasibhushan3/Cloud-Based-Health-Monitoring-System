# Cloud-Based-Health-Monitoring-System
We implemented a Cloud Based Health Monitoring Website using Django which is hosted in AWS, as a part of Cloud Computing Course in IIT Kharagpur.

#### Idea of the Project
The user enters his/her health information in the website under his account. Then a model predicts predicts the probablities of various diseases and securely stores the user's information using password based encryption.

#### Hosting in AWS
To host in AWS, we need to modify the 'settings.py' file stored in the 'cloud' folder. Please look at the 'settings.py in AWS' folder to look at the modifications of the setting.py file. (The website name must be written in ALLOWED_HOSTS of settings.py file)

This [link](https://www.youtube.com/watch?v=u0oEIqQV_-E&ab_channel=ShobiPP) is helpful for deploying a Django application to AWS.

#### Commands
```
In local PC:  'python3 manage.py runserver'
In AWS: 'python3 manage.py runserver 0.0.0.0:8000'   (It gets hosted in 8000 port)
```
#### Website
```
In local PC:  'http://localhost:8000/accounts/login/'
              'http://localhost:8000/admin'  (For Administrator which Django provides by default)
              
In AWS:  'http://__website_name__:8000/accounts/login/'  (The website name must be written in ALLOWED_HOSTS of settings.py file)
         'http://__website_name__:8000/admin'  (For Administrator which Django provides by default)
```

