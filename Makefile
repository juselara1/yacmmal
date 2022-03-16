SHELL=/bin/bash

test: test-builder test-decorator

test-builder:
	@echo "Testing builder..."
	pytest test/test_builder.py

test-decorator:
	@echo "Testing decorator..."
	pytest test/test_decorator.py
