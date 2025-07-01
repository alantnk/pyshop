# Django E-Commerce Project

### Commands

1. docker pull rabbitmq:3.10-management
2. docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.10-management 
3. celery -A config worker -l info
4. celery -A config flower --basic-auth=username:password
5. py manage.py runserver

### Servers

- **127.0.0.1:8000** Django Site
- **127.0.0.1:15672** RabbitMQ Interface
- **127.0.0.1:5555** Celery Interface