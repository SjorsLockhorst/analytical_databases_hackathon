# Dev environment & database instructions

## Prerequisit
In order to use the provided dev containter, ensure that you have installed the official "dev containers" extention for VSCode. You can find it by searching for "dev containers" in the extension marketplace in VSCode. It's the one by Microsoft. 

Next, make sure that you have installed docker and have it running on your machine. You can find instructions for your operating system [on the official site](https://docs.docker.com/engine/install/).

## Setting up the .devcontainer
Now that you have Docker running and the devcontainers plugin installted, create an `.env` file in the `.devcontainer` folder. Use the `.env_example` as an example for what the file should contain. 

After this, restart VSCode. You should get a pop-up asking you if you would like to start the dev container. Click yes and wait for the environment to load. All dependencies should be automatically installed and VSCode should have selected the correct interperter.

## Setting up PGAdmin
PGAdmin is included in the setup, which allows you to visualy inspect the database among other things. In order to use it, naviage to `http://localhost:15433/` and use the credentials in the `.env` file you created. Next, add the pg_vector server by clicking "add new server". Under the connection tab, use `localhost` and port `15432`. Username is `postgres` and the password can be found in the `.env` file.

in case you are having issues witht he above host and port, inspect the container and look for IPAddress and use that to connect with port `5432` as opposed to port 15432 :

"Networks": {
			"postgres-network": {
				"IPAMConfig": null,
				"Links": null,
				"Aliases": [
					"analytical_databases_hackathon_devcontainer-database-1",
					"database",
					"f1c89291b432"
				],
				"NetworkID": "025a537432489098b68aff96607cbd1eb59bdc2b5eae2e562522e3a4b09c9e2f",
				"EndpointID": "2ebbaf08626469c6886a042f4fd0d76adee2cf62135fe01df32c382c50bbde52",
				"Gateway": "172.18.0.1",
				"IPAddress": "172.18.0.2", , <-- THIS ONE
				"IPPrefixLen": 16,
				"IPv6Gateway": "",
				"GlobalIPv6Address": "",
				"GlobalIPv6PrefixLen": 0,
				"MacAddress": "02:42:ac:12:00:02",
				"DriverOpts": null
			}
		}

## Setting up the Django app
For you convenience a very minimal Django app has been included which automatically connects to the `pg_vector` database. This gives you a framework which you can use to write code to query the database from a webpage. 

First, make sure that you follow the above dev containers intructions so that PostgreSQL is up and running. Next run the `pg_vector_get_started.py` script. This will create the db you need for embedings and Django related things. Verify everything is working by running `python manage.py runserver`. You should be able to access the app at this point. Finally run `python manage.py migrate` to apply the standard Django migrations to the database.

Happy coding!
