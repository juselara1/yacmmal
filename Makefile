SHELL=/bin/bash
PACKAGE_NAME="yacmmal"

test: test-builder test-decorator

doc: clean-doc build-doc

publish:
	@echo "Building and publishing to Pypi..."
	poetry version `git describe --tags --abbrev=0`
	poetry build -f sdist && poetry publish

clean-doc:
	@echo "Cleaning doc files..."
	./docs/docutils clean_docs

build-doc:
	@echo "Building docs..."
	./docs/docutils build_docs "${PACKAGE_NAME}"

local-doc: doc
	@echo "Building local docs..."
	./docs/docutils local_docs

test-builder:
	@echo "Testing builder..."
	pytest test/test_builder.py

test-decorator:
	@echo "Testing decorator..."
	pytest test/test_decorator.py
