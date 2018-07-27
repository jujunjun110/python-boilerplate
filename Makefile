setup:
	PYTHONPATH="${PYTHONPATH}:${PWD}/app" pipenv run python app/tasks/setup.py
	make migrate
	make seed

migrate:
	cd db && pipenv run orator migrate -f

seed:
	cd db && pipenv run orator db:seed -f

reset-db:
	cd db && pipenv run orator migrate:refresh -f

console:
	PYTHONPATH="${PYTHONPATH}:${PWD}/app" pipenv run python -i app/tasks/console.py
		
c: console
