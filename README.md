# Coup challenge app
Find number of Fleet Engineers.

## Prerequisites

* [docker](https://docs.docker.com/), [docker-compose](https://docs.docker.com/compose/install/)
* [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) - python virtualenv
* [nose](https://pypi.org/project/nose/) - unit test
* [pyresttest](https://github.com/svanoort/pyresttest) - functional test

## Run the app

* with docker image

        > docker run -p 8080:8080 -d yervant/coup-challenge-app

* with docker-compose

        > docker-compose up --build

* with python development virtualenv

        > pip install -r requirements.txt
        > pip install .
        > coup-challenge-app


## Unit tests
        > nosetests -vs

## Functional tests
        > pyresttest http://127.0.0.1:8080/v0  functional_tests/v0.yaml

## API client library
       from v0.client import CoupChallenge
       coup_challenge = CoupChallenge()
       coup_challenge.num_of_fe ([5, 10], 12, 5)

## Swagger UI
Available at: `http://127.0.0.1:8080/v0/` when the app is running.

![image](https://user-images.githubusercontent.com/1865847/41182488-35c9c998-6b76-11e8-8de9-54bdd2c9a488.png)


