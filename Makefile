.PHONY: clean sources srpm tests

PROJECT    ?= boto
PACKAGE    := python-$(PROJECT)
VERSION    := $(shell rpm -q --qf "%{version}\n" --specfile $(PACKAGE).spec | head -1)

clean:
	@rm -rf build dist $(PROJECT).egg-info $(PROJECT)-*.tar.gz *.egg *.src.rpm

sources: clean
	@git archive --format=tar --prefix="$(PROJECT)-$(VERSION)/" \
		$(shell git rev-parse --verify HEAD) | gzip > $(PROJECT)-$(VERSION).tar.gz

srpm: sources
	@rpmbuild -bs --define "_sourcedir $(CURDIR)" \
		--define "_srcrpmdir $(CURDIR)" $(PACKAGE).spec

tests:
	@tox
