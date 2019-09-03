DEPS:=venv

export PYTHON = python3
export PYTHONPATH=$(DEPS):.

etl: rosters depth

rosters:
	$(PYTHON) rosters.py

depth: compile
	$(PYTHON) -s -m espn.depth

starters:
# starters who may be available
	echo "POSITION="
	grep "`cat data/depth/* | grep $(POSITION) | cut -f2`" data/free-agents/*

compile: $(DEPS)
$(DEPS): requirements.txt
	$(PYTHON) -m pip install -t $(DEPS) -r requirements.txt
	touch $(DEPS)
