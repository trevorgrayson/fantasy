DEPS:=venv

export PYTHON = python3
export PYTHONPATH=$(DEPS):.

default: rosters depth

rosters:
	$(PYTHON) rosters.py

depth: compile
	$(PYTHON) -s -m espn.depth

compile: $(DEPS)
$(DEPS): requirements.txt
	$(PYTHON) -m pip install -t $(DEPS) -r requirements.txt
	touch $(DEPS)
