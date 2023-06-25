VENV=.venv

$(VENV):
	python3 -m venv .venv
	.venv/bin/pip install pytest

venv: $(VENV)

test: $(VENV)
	.venv/bin/pytest -svvv tests

clean:
	rm -rf .venv
	find . -name "*.pyc" -delete
