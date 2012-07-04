spec=voms-test-ca.spec
version=$(shell grep "Version:" $(spec) | sed -e "s/Version://g" -e "s/[ \t]*//g")
release=1
rpmbuild_dir=$(shell pwd)/rpmbuild

all: rpm

dist: 
	tar cvzf voms-test-ca-$(version).tar.gz *.pem *.crl *.0 *.r0 *.signing_policy certs

rpm: clean dist
	mkdir -p $(rpmbuild_dir)/BUILD $(rpmbuild_dir)/RPMS $(rpmbuild_dir)/SOURCES $(rpmbuild_dir)/SPECS $(rpmbuild_dir)/SRPMS
	cp voms-test-ca-$(version).tar.gz $(rpmbuild_dir)/SOURCES
	rpmbuild --nodeps -v -ba $(spec) --define "_topdir $(rpmbuild_dir)"
	
clean:
	rm -rf voms-test-ca-$(version).tar.gz $(rpmbuild_dir)
