# Makefile for crpn

build:
	python -m pep517.build .

install: build
	pip install dist/crpn-0.0.1.tar.gz

clean:
	rm -r build

spotless: clean
	rm -r dist
	rm -r crpn.egg-info
