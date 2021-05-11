.DEFAULT_GOAL := help
.PHONY: deps help lint publish test tox

deps:  ## Install dependencies
	python -m pip install --upgrade pip
	python -m pip install numpy sympy matplotlib black interrogate pytest pytest-cov pytest-flake8 pytest-randomly pytest-sugar

lint:  ## Lint and static-check
	python -m black --check fractpy/
	python -m black --check tests/
	python -m interrogate fractpy
	python -m pytest --cache-clear --flake8 fractpy

publish:  ## Publish to PyPi
	python -m flit publish

test:  lint	## Run tests
		python -m pytest --cache-clear --flake8 tests

tox:   ## Run tox
	python -m tox

help: ## Show help message
	@IFS=$$'\n' ; \
	help_lines=(`fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##/:/'`); \
	printf "%s\n\n" "Usage: make [task]"; \
	printf "%-20s %s\n" "task" "help" ; \
	printf "%-20s %s\n" "------" "----" ; \
	for help_line in $${help_lines[@]}; do \
		IFS=$$':' ; \
		help_split=($$help_line) ; \
		help_command=`echo $${help_split[0]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
		help_info=`echo $${help_split[2]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
		printf '\033[36m'; \
		printf "%-20s %s" $$help_command ; \
		printf '\033[0m'; \
		printf "%s\n" $$help_info; \
	done