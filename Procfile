release: python3 manage.py migrate --noinput
web: gunicorn motiflash.wsgi --log-file - -c gunicorn.conf