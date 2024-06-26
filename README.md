
# Chat App

## Guide

1. Sign up forms: apps\templates\accounts\register_view.html
2. Websockets configuration and chat logic: apps\web\apps\chat\consumers.py
3. Redis caching: apps\web\backend\cache\redis_cache.py
4. Tests: apps\web\apps\chat\tests.py and apps\web\apps\accounts\tests.py
5. Throttling configuration: apps\web\backend\settings\base.py
6. Logging and monitoring: apps\web\backend\settings\base.py


## Install:


1. Create a virtual environment.

```bash
python -m venv ./env
source env/bin/activate
```

2. Install requirements
```bash
python -m pip install pip --upgrade
python -m pip install -r requirements.txt
```

3. Rename .env.sample to .env and add your keys:

Replace  `SECRET_KEY` with a new one:

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

4. Build and start the docker file:

```bash
docker compose -f docker-compose.selfhost.yaml build
docker compose -f docker-compose.selfhost.yaml up
```

5. Django migrations
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

8. Build frontend.

```bash
npm run bootstrap
```

## App

![image](https://github.com/Phelyxx/chat-app/assets/41241094/bb91a8ac-6fed-4a3e-92b2-9bba83fd497d)

![image](https://github.com/Phelyxx/chat-app/assets/41241094/42c9a747-1ffd-4f43-abf1-ad271743e160)

![image](https://github.com/Phelyxx/chat-app/assets/41241094/2e1f9209-3512-4a9b-98d0-3b98eeac0125)

