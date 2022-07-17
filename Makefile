install:
	poetry install

test:
	poetry run pytest

run:
	poetry run gendiff

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

test-coverage:
	poetry run pytest --cov=hexlet_python_package --cov-report xml

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

build:
	poetry build

