create_venv:
	python3 -m venv venv

setup_env:
	. venv/bin/activate
	pip install -r requirements.txt
	. .conf

dev:
	. .conf
	heroku local

spec:
	. .conf
	python -m pytest -vv
