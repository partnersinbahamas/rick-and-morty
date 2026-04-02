# How to run the project
- Create venv `python -m venv venv`
- Activate venv `source venv/bin/activate`
- Build docker image `docker-compose build`
- Run Docker container `docker-compose uo`
- Install requirements `pip install -r requirements.txt`
- Run migrations `python manage.py migrate`
- Run Celery tasks worker `celery -A app worker -l INFO`
- Run Django Celery Beat `celery -A app beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler`
- Done