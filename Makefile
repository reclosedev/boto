MAIN_TREE := HEAD
MAIN_COMMIT := $(shell git rev-parse --verify $(MAIN_TREE))
BOTO := boto

sources:
	@git archive --format=tar --prefix="$(BOTO)/" $(MAIN_COMMIT) | gzip > "$(BOTO).tar.gz"
