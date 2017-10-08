PROJECT_DIR=integra_ti
MANAGE=python $(PROJECT_DIR)/manage.py

help:
	@echo "test - run tests"
	@echo "install - install Python dependencies"
	@echo "db - create and migrate database"
	@echo "run - run server"


install:
	pip install -r requirements.txt

db:
	$(MANAGE) migrate

test:
	$(MANAGE) test

run:
	$(MANAGE) runserver 