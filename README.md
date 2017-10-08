# IntegraTI


[![Build Status](https://travis-ci.org/sarahraquel/IntegraTI.svg?branch=master)](https://travis-ci.org/sarahraquel/IntegraTI)



-------------
#### Requirements
* Python 3.6+
* Virtualenvwrapper

-------------
#### Set Up
Clone this project and create the virtual environment:
~~~~bash
$ git clone https://github.com/sarahraquel/IntegraTI.git
$ mkvirtualenv integravenv
$ workon integravenv
~~~~
Install all dependencies
~~~~bash
$ make install
~~~~
Setup database:
~~~~bash
$ make db
~~~~
Testing:
~~~~bash
$ make test
~~~~

Running the app:
~~~~bash
$ make run
~~~~
You can now go to [http://localhost:8000](http://localhost:8000).