setup_env:
	python3 -m venv venv
	. venv/bin/activate
	pip install -r requirements.txt

dev:
	heroku local

spec:
	python -m pytest -vv
