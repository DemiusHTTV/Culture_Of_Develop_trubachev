PHONY: create-practice remove practice
create-practice:
       mkdir -p $(NAME)/Makefile
	   cp MakePracticefile $(NAME)/Makefile
remove-practice:
       rm -rf $(NAME)