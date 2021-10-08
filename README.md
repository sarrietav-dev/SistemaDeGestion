# SistemaDeGestion
Reto para el ciclo 3 MisionTIC 2022

Quickstart
----------


First, set your app's secret key as an environment variable. For example,
add the following to ``.env``.

    export SECRET_KEY='something-really-secret'

Before running shell commands, set the ``FLASK_APP`` and ``FLASK_DEBUG``
environment variables:

    export FLASK_APP=/web/app.py
    export FLASK_DEBUG=1

Then run the following commands to bootstrap your environment:

    git clone https://github.com/CAMINO-Murillo/SistemaDeGestion
    cd SistemaDeGestion
    pip install -r requirements/development.txt


To start Docker Machine, first make sure you’re in the project root and then simply run:
this command:

    docker-machine create -d virtualbox dev;

The create command setup a “machine” (called dev) for Docker development.
In essence, it downloaded boot2docker and started a VM with Docker running.
Now just point the Docker client at the dev machine via:

    eval "$(docker-machine env dev)"

Now, to get the containers running, build the images and then start the services:

    docker-compose up --build -d

We also need to create the database table:

    docker-compose run web /usr/local/bin/python create_db.py

Deployment
----------

In your production environment, make sure the ``FLASK_DEBUG`` environment
variable is unset or is set to ``0``, so that ``BaseConfig`` is used, and
set ``DATABASE_URL`` which is your postgresql URI for example
``postgresql://localhost/example`` (this is set by default in heroku).


Shell
-----

To open the interactive shell, run:

    flask shell

By default, you will have access to the flask ``web`` and models.


Running Tests
-------------

To run all tests, run:

    flask test


Deployment to cloud
----------

So, with our app running locally, we can now push this exact same environment to a cloud hosting provider with Docker Machine.
Let’s deploy to a Digital Ocean droplet.

After you sign up for Digital Ocean, generate a Personal Access Token, and then run the following command:

    docker-machine create \
    -d digitalocean \
    --digitalocean-access-token ADD_YOUR_TOKEN_HERE \
    production

Then set production as the active machine and load the Docker environment into the shell:

    eval "$(docker-machine env production)"

Finally, let’s build the Flask app again in the cloud:

    docker-compose build
    docker-compose up -d
    docker-compose run web /usr/local/bin/python create_db.py
