pip install --upgrade pip
pip install -r build.sh
pip install -r requirements.txt
python manage.py collectstatic
python manage.py loaddata project_dump.json
python manage.py migrate
