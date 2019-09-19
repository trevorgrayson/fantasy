PYDEPS:=venv

export PYTHON = python3
export PYTHONPATH=$(PYDEPS):.

etl: compile rosters depth
	git add data
	git commit -m "`date`"

depth_check: compile
	./bin/new_first_strings | ./bin/depth_check

availability: compile
	./bin/new_first_strings | ./bin/availablity

rosters: compile
	$(PYTHON) rosters.py

depth: compile
	$(PYTHON) -s -m espn.depth

starters:
# starters who may be available
	echo "POSITION="
	grep "`cat data/depth/* | grep $(POSITION) | cut -f2`" data/free-agents/*

compile: $(PYDEPS)
$(PYDEPS): requirements.txt
	$(PYTHON) -m pip install -t $(PYDEPS) -r requirements.txt
	touch $(PYDEPS)

clean:
	rm -rf $(PYDEPS)
