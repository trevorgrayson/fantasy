DEPS:=venv

export PYTHON = python3
export PYTHONPATH=$(DEPS):.

etl: rosters depth
	git add data
	git commit -m "`date`"

depth_check:
	./bin/new_first_strings | ./bin/depth_check

availability:
	./bin/new_first_strings | ./bin/availablity

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
