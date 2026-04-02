# How to run the project
- Create venv `python -m venv venv`
- Activate venv `source venv/bin/activate`
- Create a `.env` file in the project root using `.env.example`:

    ### .env
    ```env
    POSTGRES_DB=db
    POSTGRES_USER=user
    POSTGRES_PASSWORD=password
    POSTGRES_HOST=localhost
    POSTGRES_PORT=5436
    PGDATA=/var/lib/postgresql/data
  
    CELERY_BROKER_URL=url
    CELERY_RESULT_BACKEND=url
    
    DJANGO_SECRET_KEY=secret-key
    DJANGO_ENV=.env
    ```
    
    ### .env.docker
    ```.env.docker
    POSTGRES_DB=db
    POSTGRES_USER=user
    POSTGRES_PASSWORD=password
    POSTGRES_HOST=db
    POSTGRES_PORT=5432
    PGDATA=/var/lib/postgresql/data
  
    CELERY_BROKER_URL=url
    CELERY_RESULT_BACKEND=url
    
    DJANGO_SECRET_KEY=secret-key
    DJANGO_ENV=.env.docker
    ```

- Build docker image `docker-compose build`
- Run Docker container `docker-compose up`
- Install requirements `pip install -r requirements.txt`
- Run migrations `python manage.py migrate`
- Run Celery tasks worker `celery -A app worker -l INFO`
- Run Django Celery Beat `celery -A app beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler`
- Done