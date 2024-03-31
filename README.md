# Flow - Backend API
![Project-image](https://github.com/EmilionR/pp5-frontend/blob/main/documentation/responsive.png)

Flow is an image-sharing social media site. Users can post images, comment on posts, and follow other users.
Users can also create personal feeds by following other users and liking posts. They can also hide unwanted content, block users, create their own inner circle of selected followers, and more.

[View the website here](https://emil-pp5-frontend-9557540625e4.herokuapp.com/)

## Contents

* [General Information](#general-information)
* [Testing](#testing)
* [Deployment](#deployment)
  * [GitHub](#github)
  * [Heroku](#heroku)

## General Information

You can find detailed information in [the pp5 Front-end repo](https://github.com/EmilionR/pp5-frontend). For testing data, 

## Testing
For testing data, [see the testing file](TESTING.md)

## Deployment

### Heroku

__Project Settings:__

* Include ```https://<your_app_name>.herokuapp.com``` in the ALLOWED_HOSTS and CSRF_TRUSTED_ORIGINS lists inside the settings.py file.
* Make sure that the environment variables (DATABASE_URL, SECRET_KEY, and CLOUDINARY_URL) are correctly set to ```os.environ.get("<variable_name>")```
* If making changes to static files or apps, make sure to run collectstatic or migrate as needed.
* Commit and push to the repository.

__Requirements__

In order to deploy the API, Heroku needs information about the technologies used. Before deployment, I create a list of requirements in a file called. In some cases, you may also need a runtime.txt file specifying the version of Python to use.

* Create a plain file called Procfile without any file suffix, at the root level of the project.
* Type ```web: gunicorn fooroom.wsgi:application``` into the Procfile and save.
* In your IDE terminal, type ```pip3 freeze local > requirements.txt``` to create the requirements.
* (Optional) Create a runtime.txt and type ```python-3.12.1``` (or whichever version you use)
* Commit and push these files to the project repository.

__Heroku Settings:__

For Heroku to be able to process and render the project, you must define some environment variables.
Deploying the project without these is like trying to start a car without the key.

* Go to the settings page of your new app
* Scroll down and open the Config Vars
* Add a DATABASE_URL variable and assign it a link to your database
* Add a SECRET_KEY variable and assign it a secret key of your choice
* Add a CLOUDINARY_URL variable and assign it a link to your Cloudinary
* Add an ALLOWED_HOST variable and assign it the url of the deployed heroku link
* Add a CLIENT_ORIGIN variable and assign it the url of your deployed frontend app
* Adda a CLIENT_ORIGIN_DEV variable and assign it the url of your local development client

__Connect the repository__

Once your Heroku settings and GitHub repository are up to date, it's time to connect the two.

* Go to the Deploy tab of your Heroku app.
* Find the "Deployment method" section and click GitHub.
* Type in the name of your repository to search for it
* Click 'Connect' to connect the repository
* (Optional) Enable automatic deployment to automatically update the Heroku app whenever you push to GitHub

__Deploy the project to Heroku__

Now, all that's left to do is to deploy and open the app.

* Click "Deploy branch"
* Wait for Heroku to finish building the app.
* Upon successful deployment, click the "View" button to open the app.

### GitHub

__How to Fork the Repository__

1. Log in (or sign up) to GitHub.
2. Go to the repository for this project, [EmilionR/pp5-api](https://github.com/EmilionR/pp5-api)
3. Click the Fork button in the top right corner.

__How to Clone the Repository__

1. Log in (or sign up) to GitHub.
2. Go to the repository for this project, [EmilionR/pp5-api](https://github.com/EmilionR/pp5-api)
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.