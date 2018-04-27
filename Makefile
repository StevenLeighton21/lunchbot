setup_env:
	python3 -m venv venv
	. venv/bin/activate
	pip install -r requirements.txt

dev:
	export FLASK_APP=main.py ; python main.py

spec:
	python -m pytest -vv
