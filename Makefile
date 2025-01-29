dockerup:
	sudo docker compose -f docker-compose.yml up -d --build

dockerdown:
	sudo docker compose -f docker-compose.yml down

createsuperuser:
	python3 app/manage.py createsuperuser

makemigrations:
	python3 app/manage.py makemigrations

migrate:
	python3 app/manage.py migrate

runserver:
	python3 app/manage.py runserver
