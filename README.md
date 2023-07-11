# [onetimesecret](https://onetimesecret.com/) analog

## Features

* **FastAPI** backend, asynchronous JsonAPI service
* **Redis** as database, asynchronous pipeline
* **Docker** integration
* **Docker Compose** integration

## Launch

* Build docker containers
```
make build
```
* Run docker containers
```
make up
```
* Open container shell
```
make <app/db>-shell
```
* Stop docker containers
```
make down
```

## Endpoints

* The `/generate` method accepts a secret and a **passphrase** and gives the **secret_key** by which the secret can be obtained.
* The `/secrets/{secret_key}` method takes a **passphrase** as input and gives the secret.

To see interactive API documentation open [http://0.0.0.0:8000/docs](http://0.0.0.0:8000/docs)