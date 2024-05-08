.DEFAULT_GOAL := build
VERSION = 1.1.10

image:
	docker pull python:3.9
	docker pull python:3.9-slim
	docker build -t docker.heggi.org/cashit/site:$(VERSION) .
	docker image prune -f

push:
	docker push docker.heggi.org/cashit/site:$(VERSION)
