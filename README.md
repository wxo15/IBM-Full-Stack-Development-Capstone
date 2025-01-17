# IBM Full Stack Cloud Development Capstone

This is a capstone project for IBM Full Stack Cloud Developer Professional Certificate.

![screenshot](https://github.com/wxo15/IBM-Full-Stack-Development-Capstone/blob/master/how-it-works.gif)

## Links
[IBM Full Stack Cloud Developer Professional Certificate](https://www.coursera.org/professional-certificates/ibm-full-stack-cloud-developer)

[Link to CF App](http://dealerreiew-707.us-south.cf.appdomain.cloud/djangoapp)

[Link to CF Admin page](http://dealerreiew-707.us-south.cf.appdomain.cloud/admin)

[Link to Heroku Container App](https://dealer-review.herokuapp.com/djangoapp)

[Link to Heroku Container Admin page](https://dealer-review.herokuapp.com/admin)

## Description
This is a Django app built to allow users to read reviews for cars for each dealership. A user can sign up and login to the application using Django user authentication system, which allows them to add reviews to existing car models and make. Admin can add models and makes on the admin page. The sentiment of the review is analysed using Watson Natural language Understanding service. New reviews are added to a IBM Cloudant database through a custom API, to be retrieved when needed. Car model and car make is managed through Django ORM, while reviews and dealershps are stored in Cloudant, accessed using custom APIs.

This project is pushed to Cloud Foundary.

## How-tos
### How to run
1. Clone repo.
2. Navigate to /server.
3. Run `pip3 install -r requirements.txt`.
4. Make a root user by running `python3 manage.py createsuperuser`.
5. Run `python3 manage.py makemigrations`.
6. Run `python3 manage.py migrate --run-syncdb`.
7. Run `python3 manage.py runserver` to run server. By default, it will use port 8000. Go to /djangoapp for the app itself, or /admin to access Django administration page.

### How to push to Cloud Foundary
1. Install IBM CLI tool [here](https://cloud.ibm.com/docs/cli?topic=cli-getting-started). Install cf tools using `ibmcloud cf install`.
2. Login to IBM cloud on CLI by running `ibmcloud login -u <email>`.
3. Get account details by running `ibmcloud account orgs`.
4. Target Cloud Foundary by running `ibmcloud target --cf-api https://api.<region>.cf.cloud.ibm.com -r <region> -o <account_owner>`.
5. Make and target a "djangoserver" space using `ibmcloud account space-create djangoserver-space` and `ibmcloud target -s djangoserver-space`.
6. Make sure `manifest.yml` and `djangoproject/settings.py` are correct.
7. Run `ibmcloud cf push`.

### How to push Docker image to Heroku
1. Clone repo to your machine and navigate to server folder in your terminal.
2. Install `heroku` and `docker` on your machine.
3. Login to heroku on your CLI by running `heroku login` and then `heroku container:login`.
4. Create a container app by running `heroku create`, `heroku stack:set container --app APP`
5. Go to server/Dockerfile and change 2 instances of `8000` to `$PORT`. This will be assigned by Heroku upon image push.
6. Go to server/djangobackend/settings.py and add your app's host to ALLOWED_HOST.
7. Run `python3 manage.py makemigrations` and then `python3 manage.py migrate --run-syncdb` to make sure all changes have been migrated.
8. Make a root user by running `python3 manage.py createsuperuser`.
9. Run 'heroku container:push web --app=APP', and if it goes successfully, `heroku container:release web --app=APP` to push and release the app to heroku.
10. Navigate to your APP + "/djangoapp" to make sure it is running.

