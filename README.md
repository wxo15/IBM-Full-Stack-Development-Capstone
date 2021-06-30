# IBM Full Stack Cloud Development Capstone

This is a capstone project for IBM Full Stack Cloud Developer Professional Certificate.

![screenshot](https://github.com/wxo15/IBM-Full-Stack-Development-Capstone/blob/master/how-it-works.gif)

## Links
[IBM Full Stack Cloud Developer Professional Certificate](https://www.coursera.org/professional-certificates/ibm-full-stack-cloud-developer)

[Link to App](http://dealerreiew-707.us-south.cf.appdomain.cloud/djangoapp)

[Link to Admin page](http://dealerreiew-707.us-south.cf.appdomain.cloud/admin)

## Description
This is a Django app built to allow users to read reviews for cars for each dealership. A user can sign up and login to the application using Django user authentication system, which allows them to add reviews. The sentiment of the review is analysed using Watson Natural language Understanding service. New reviews are added to a IBM Cloudant database through a custom API, to be retrieved when needed. Car model and car make is managed through Django ORM, while reviews and dealershps are stored in Cloudant, accessed using custom APIs.

This project is pushed to Cloud Foundary.
