# Django E-Commerce Project

## Demo
[![YouTube Video kJ6BMQCWCOg](https://utfs.io/f/nGnSqDveMsqxOUdLxp0k5fKEn2LbBoPAuZ6XMTHDcNJ0QiG1)](https://www.youtube.com/watch?v=ZKt5pkfC6Yw)

## Setup

### RabbitMQ (Docker) 
1. docker pull rabbitmq:3.10-management
2. docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.10-management 

### Redis (Docker)
1. docker pull redis:8-bookworm
2. docker run -it --rm --name redis -p 6379:6379 redis:8-bookworm

### Stripe
1. stripe login
2. stripe listen --forward-to 127.0.0.1:8000/payment/webhook/

### Celery
1. celery -A config worker -l info

### Django

1. python3 manage.py migrate
2. python3 manage.py runserver

## Servers

- **127.0.0.1:8000** Django Site
- **127.0.0.1:8000/rosetta** Translations Admin Panel
- **127.0.0.1:15672** RabbitMQ Interface

## Celery UI (OPTIONAL)
1. celery -A config flower --basic-auth=username:password
2. **127.0.0.1:5555** Celery Interface



