pip install -r build.sh
python manage.py loaddata project_dump.json
python manage.py migrate
#pip install -r requirements.txt