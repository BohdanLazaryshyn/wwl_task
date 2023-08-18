## WWL task
Its simple task for Producer - Consumer problem.

### Features
* Register, login, logout
* Send message to telegram bot after deleting order
* Schedule task for creating order

### Used technologies
* Python 3.11
* Django
* PostgreSQL
* Docker
* Docker-compose
* Celery
* Redis
* Telegram bot

### How to run without docker 
* git clone https://github.com/BohdanLazaryshyn/wwl_task
* python -m venv venv
* venv\Scripts\activate (on Windows)
* source venv/bin/activate (on macOS)
* pip install -r requirements.txt
* create .env file (see below)
* python manage.py migrate
* python manage.py runserver

### You should have create .env file:
```
SECRET_KEY=your_secret_key
BOT_TOKEN=your_token
CHAT_ID=your_chat_id
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
POSTGRES_DB=your_db
POSTGRES_HOST=your_host
```

### How to run with docker
*docker-compose up --build*

### Hosts
* http://127.0.0.1:8000

### You can use this command for load data to db (after migrate)
* python manage.py loaddata data.json
