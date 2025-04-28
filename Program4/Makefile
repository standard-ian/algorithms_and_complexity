.PHONY: run test git

EXEC=min_sum.py
TEST=test_$(EXEC)
MAKE=Makefile
IGNORE=.gitignore

run:
	./$(EXEC)

test:
	pytest -sv --benchmark-compare

git:
	git add $(EXEC) $(TEST) $(MAKE) README.md conftest.py $(IGNORE)
	git commit
	git push

