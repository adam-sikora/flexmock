
color := $(shell tput setaf 2)
off := $(shell tput sgr0)
PYTHON := $(if $(shell command -v python3),python3,python)
TARGETS = src tests

.PHONY: all
all: lint test

.PHONY: lint
lint: isort black mypy pylint

.PHONY: test
test: install twisted unittest pytest

.PHONY: install
install:
	@printf '\n\n*****************\n'
	@printf '$(color)Install flexmock$(off)\n'
	@printf '*****************\n'
ifeq (${VIRTUAL_ENV},)
	@printf 'Skipping install. VIRTUAL_ENV is not set.\n'
else
	pip install .
endif


.PHONY: pytest
pytest:
	@printf '\n\n*****************\n'
	@printf '$(color)Running pytest$(off)\n'
	@printf '*****************\n'
	pytest tests/flexmock_pytest_test.py

.PHONY: unittest
unittest:
	@printf '\n\n*****************\n'
	@printf '$(color)Running unittest$(off)\n'
	@printf '*****************\n'
	$(PYTHON) -m unittest tests/flexmock_test.py

.PHONY: twisted
twisted:
	@printf '\n\n*****************\n'
	@printf '$(color)Running twisted tests$(off)\n'
	@printf '*****************\n'
	$(PYTHON) -c "from twisted.scripts.trial import run; run();" tests/flexmock_pytest_test.py

.PHONY: mypy
mypy:
	@printf '\n\n*****************\n'
	@printf '$(color)Running mypy$(off)\n'
	@printf '*****************\n'
	mypy ${TARGETS}

.PHONY: isort
isort:
	@printf '\n\n*****************\n'
	@printf '$(color)Running isort$(off)\n'
	@printf '*****************\n'
	isort --check-only ${TARGETS}

.PHONY: black
black:
	@printf '\n\n*****************\n'
	@printf '$(color)Running black$(off)\n'
	@printf '*****************\n'
	black --check ${TARGETS}

.PHONY: pylint
pylint:
	@printf '\n\n*****************\n'
	@printf '$(color)Running pylint$(off)\n'
	@printf '*****************\n'
	pylint ${TARGETS}
