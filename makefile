coverage:
	python -m pytest -v --cov-report term-missing --cov=heimdall_logger/ --cov-report=xml

test:
	python -m pytest

list-requirements:
	pip freeze

install-requirements:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt
