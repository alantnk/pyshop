# Django E-Commerce Project

## Commands

### RabbitMQ (Docker) 
1. docker pull rabbitmq:3.10-management
2. docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.10-management 


### Redis (Docker)
1. docker pull redis:8-bookworm
2. docker run -it --rm --name redis -p 6379:6379 redis:8-bookworm


### Celery
1. celery -A config worker -l info
2. celery -A config flower --basic-auth=username:password (OPTIONAL)

### Stripe
1. stripe login
2. stripe listen --forward-to 127.0.0.1:8000/payment/webhook/

### Django

1. python3 manage.py runserver

## Servers

- **127.0.0.1:8000** Django Site
- **127.0.0.1:15672** RabbitMQ Interface
- **127.0.0.1:5555** Celery Interface (OPTIONAL)