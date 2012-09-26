SUBDIRS = voms-test-ca igi-test-ca
CLEANDIRS = $(SUBDIRS:%=clean-%)

.PHONY: subdirs $(SUBDIRS)

subdirs: $(SUBDIRS)
clean: $(CLEANDIRS)
all: subdirs

$(SUBDIRS):
	$(MAKE) -C $@

$(CLEANDIRS): 
	$(MAKE) -C $(@:clean-%=%) clean
