build:
	docker-compose build
up:
	docker-compose up -d
down:
	docker-compose down
%-shell:    # replace % with "app" to get app's shell or with "db" to get db's shell
	docker-compose exec $* bash
	