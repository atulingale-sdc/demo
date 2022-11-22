# DEMO-BACKEND

Backend for DEMO

## Getting started

```
git clone https://github.com/atulingale-sdc/demo.git
cd demo
```

## Install Redis
```
sudo apt-get update
sudo apt install redis
redis-cli --version
sudo systemctl status redis
```

## Install Pipenv
```
sudo apt install python3-pip
python3 -m pip install --user pipenv
```


# Setup auth service
```
cd services/auth-service/ && pipenv install
pipenv shell
export PYTHONPATH=.
alembic upgrade heads
python auth_service &
```

```
to access auth service visit - http://127.0.0.1:7070/docs
```

# Setup weather service
```
cd services/weather-service/ && pipenv install
pipenv shell
alembic upgrade heads
python weather_service &
```
```
to access weather service visit - http://127.0.0.1:7074/docs
```

## login credentials
```
atul@demo.com / admin@123
```
