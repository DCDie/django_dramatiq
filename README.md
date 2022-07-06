# 📱 Example of use in one project django-dramatiq and django-apscheduler

Rest API project with Dramatiq and Apscheduler

### 📝 Requirements

1. Python 3.10
2. Dramatiq
3. Apscheduler
4. RabbitMQ
5. Redis

### 🔧 .env

```
# Django
SECRET_KEY=

# Email settings
EMAIL_BACKEND=
EMAIL_HOST=
EMAIL_USE_TLS=
EMAIL_PORT=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=

# Redis
REDIS_URL=

# Broker
BROKER_URL=

# Database
DATABASE_NAME=
DATABASE_USER=
DATABASE_PASSWORD=
DATABASE_HOST=
DATABASE_PORT=
```

### Deployment

#### Prepare

``` python
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```

#### Django

``` python
python manage.py runserver
```

#### Dramatiq

``` python
python manage.py rundramatiq
```

#### Apscheduler

``` python
python manage.py runapscheduler
```