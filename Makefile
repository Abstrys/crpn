# Makefile for crpn

build:
	python -m pep517.build .

install: build
	pip install dist/crpn-0.1.0.tar.gz

uninstall:
	pip uninstall crpn

clean:
	rm -r build

spotless: clean
	rm -r dist
	rm -r crpn.egg-info
