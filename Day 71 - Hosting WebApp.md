2026-03-28 00:45

Status: incomplete

Tags: [[Day 70 - Git, Github and Version Control]]


# **WSGI Server**
While our flask server is good for development and testing it is not nearly good enough for for production, in production we use a WSGI which stands for Web Server Gateway Interface
#### syntax


## References
[WSGI PyDocs](https://peps.python.org/pep-3333/)
 Essentially, a WSGI server standardises the language and protocols between our Python Flask application and the host server.

There are many WSGIs to choose from, but we'll use the most popular - [**gunicorn**](https://docs.gunicorn.org/en/stable/). That way our hosting provider will call gunicorn to run our code.
Add gunicorn to the environment requirement.txt file
and create a Procfile which contains configuration for gunicorn
```Procfile
web: gunicorn main:app
```
This will tell the hosting provider to create a web worker that is able to receive HTTP requests. The Procfile also says to use gunicorn to server the web app. And finally it specifies the Flask **app** object is the **main.py** file. That way the hosting provider knows about the entry point for the app and what our app is called.

After setting up the Procfile, push the repo to a remote repository and create an account with a hosting provider.

Create a new postgresdb and use it's internal url as your db uri