NO_COLOR=\033[0m
OK_COLOR=\033[32;01m
ERROR_COLOR=\033[31;01m
WARN_COLOR=\033[33;01m

RAML2HTML=@docker run --rm -v `pwd`:/data letsdeal/raml2html\:6.2 -i "docs/api.raml"
WEB_DOCS=docs/web

help:
	@echo "---------------------------------------------"
	@echo "List of available targets:"
	@echo "  api_docs                 - Generate API endpoints documentation"
	@echo "  hijack                   - Get inside the container"
	@echo "  start_api                - Start api engine"
	@echo "  migrate_db               - Migrate db"
	@echo "  create_migration         - Create migration file"
	@echo "  clean_cache              - Delete cache file"
	@echo "  setup_api                - Setup api for the first time"
	@echo "  restart_api              - Restart api"
	@echo "  tests                    - Run api unit tests"
	@exit 0

api_docs:
	@echo "$(OK_COLOR)==> Generating API endpoints documentation...$(NO_COLOR)"
	${RAML2HTML} -o ${WEB_DOCS}/index.html
	@echo "$(OK_COLOR)==> Done...$(NO_COLOR) Docs are available at ${WEB_DOCS}/index.html"

hijack:
	@echo "$(OK_COLOR)==> Hijacking container...$(NO_COLOR)"
	docker run -it djangoapi_api bash
	@echo "$(OK_COLOR)==> Done...$(NO_COLOR)"

start_api:
	@echo "$(OK_COLOR)==> Starting api engines...$(NO_COLOR)"
	docker-compose up -d
	@echo "$(OK_COLOR)==> Done...$(NO_COLOR)"

migrate_db:
	@echo "$(OK_COLOR)==> Starting migrating db...$(NO_COLOR)"
	docker-compose run api python manage.py migrate
	@echo "$(OK_COLOR)==> Done...$(NO_COLOR)"
	docker-compose restart

create_migration:
	@echo "$(OK_COLOR)==> Creating migration files...$(NO_COLOR)"
	docker-compose run api python manage.py makemigrations
	@echo "$(OK_COLOR)==> Done...$(NO_COLOR)"

clean_cache: hijack
	@echo "$(OK_COLOR)==> Cleaning cache files...$(NO_COLOR)"
	find . -type d -name __pycache__ -exec rm -rf {} +
	@echo "$(OK_COLOR)==> Done...$(NO_COLOR)"

restart_api:
	docker-compose restart

setup_api: start_api restart_api migrate_db

tests:
	@echo "$(OK_COLOR)==> Running unit tests...$(NO_COLOR)"
	docker-compose run app python manage.py test
	@echo "$(OK_COLOR)==> Done...$(NO_COLOR)"
