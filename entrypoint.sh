python manage.py collectstatic --no-input

gunicorn portfolio.wsgi:application --bind 0.0.0.0:8000
