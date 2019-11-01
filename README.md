##  HEALTH APPLICATION

## Description
This is a web application that allows users to create account by registering themselves into the appliaction.The user is thereby allowed to view health articles and aslo allowed to add any category of health articles of their choice. 


### By  a team of four members namely:
* Steve Mwanza - Scrum master
* Fatuma Ali - Fullstack developer
* Dickson Kariuki - Fullstack developer
* Faith Okoth - Fullstack developer

The user can:

* See various health articles on the application
* View articles category posts they like
* See the latests posts
* Generate quotes from various historic people e.g mBjarne Stroustrup.


## Setup/Installation Requirements

* python3.6
* pip
* Virtual environment(virtualenv)

## Cloning and running
Clone the application using git clone(this copies the app onto your device). In terminal:

    *  $ git clone https://github.com/Steve-design/Strike-Out
    * $ cd Strike-Out

Creating the virtual environment

   * $ python3.6 -m venv --without-pip virtual
   * $ source virtual/bin/env
   * $ curl https://bootstrap.pypa.io/get-pip.py | python

Installing Flask and other Modules

   * $ python3.6 -m pip install Flask
   * $ python3.6 -m pip install Flask-Bootstrap
   * $ python3.6 -m pip install Flask-Script
   * $ python3.6 -m pip install -r requirements.txt
   * $ python3.6 -m pip install flask-login

Run the application:

  *  $ chmod a+x start.sh
  *  $ ./start.sh

## Testing the Application

To run the tests for the class files:

  *  $ python3.6 manage.py test
## Technologies Used
* Python 3.6
* Flask

## Specifications
|Behaviour       | Input        | Output             |
|----------------|--------------|--------------------|
|Display latest blogs|	On page load|A 	list of various health articles appears|
|Registration |	Submit regitration form|	User creates an account and receives welcome email|
|Edit posts |	Submit edit post|	The post is updated with new data from user|
|New Quotes	 |Click new quotes	|it takes you to another page with random quotes|
|Adding comments|	Click create comment|	Comment is created|
 ## Support and contact details

For any questions or contributions, find us on:

Email: 
* okothfaith94@gmail.com
* smzalendo31@gmail.com


## License
MIT License Copyright (c) {2019} healthapp