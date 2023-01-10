First time setup
```
docker compose up db 
CTRL-C
docker compose up
#in new tab
docker compose exec web bash
 - python manage.py migrate
 - python manage.py createsuperuser
 - exit
```