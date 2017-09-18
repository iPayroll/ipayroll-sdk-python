help:
	@echo "  env         install all production dependencies"
	@echo "  clean       remove unwanted stuff"
	@echo "  build       build pacakge"

env:
	pip install -Ur requirements.txt

info:
	@python --version
	@pyenv --version
	@pip --version

clean:
	rm -fr build
	rm -fr dist
	rm -fr *.egg-info
	find . -name '*.pyc' -exec rm -f {} \;
	find . -name '*.pyo' -exec rm -f {} \;
	find . -name '*~' ! -name '*.un~' -exec rm -f {} \;

build: clean
	python setup.py check
	python setup.py sdist
	python setup.py bdist_wheel
