RUN:
	@echo AIRFLOW_UID=$(id -u) > .env
	@docker-compose up -d --build

clean:
	@docker-compose down 
	@docker system prune
