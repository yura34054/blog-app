makemigrations:
	python src/manage.py makemigrations
	sudo chown -R ${USER} src/app/migrations/

migrate:
	python src/manage.py migrate $(if $m, api $m,)

dev:
	python src/manage.py runserver localhost:8000

piplock:
	pipenv install
	sudo chown -R ${USER} Pipfile.lock

piplock_dev:
	pipenv install --dev
	sudo chown -R ${USER} Pipfile.lock

lint:
	isort .
	flake8 --config setup.cfg
	black --config pyproject.toml .

check_lint:
	isort --check --diff .
	flake8 --config setup.cfg
	black --check --config pyproject.toml .
