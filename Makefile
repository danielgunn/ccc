.PHONY: help test data

.DEFAULT: help

DATADIR := y2019/all_data
ZIP := $(DATADIR).zip

help:
	@echo "make data"
	@echo "   download test data"
	@echo "make test"
	@echo "   run tests"
	@echo "make clean"
	@echo "   erase test data"

data : $(ZIP)
	unzip -n -d $(dir $<) $<

$(ZIP):
	wget -O $@ -nc https://www.cemc.uwaterloo.ca/contests/computing/2019/stage%201/all_data.zip

test:	data
	python test.py

clean:
	rm -f $(ZIP)
	rm -rf $(DATADIR)
