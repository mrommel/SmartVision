# SmartVision

## run the server with 
python manage.py runserver

=> server will run at: http://127.0.0.1:8000/

## migrations

python manage.py migrate

## history of vision
python -m django --version
django-admin startproject smartvision
python manage.py startapp vision

python manage.py makemigrations vision
python manage.py sqlmigrate vision 0001
python manage.py migrate


## history of imagevision

python manage.py makemigrations imagevision
python manage.py sqlmigrate imagevision 0001
python manage.py migrate