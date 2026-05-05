.DEFAULT_GOAL := help

create-practice:	
ifndef PRACTICE
	$(error must pass val via PRACTICE)
endif
	@echo "Creating practice"
	mkdir -p $(PRACTICE)
	cp MakePracticefile $(PRACTICE)/Makefile

remove-practice:
ifndef PRACTICE
	$(error must pass val via PRACTICE)
endif
	rm -rf $(PRACTICE)

help:
	@echo "This makefile for repo-level activity"