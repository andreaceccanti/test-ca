Name: igi-test-ca
Version: 3.0.3
Release: 0%{?dist}
Summary: A test CA for IGI

Group: Applications/Internet
License: ASL 2.0
URL: https://github.com/italiangrid/test-ca

Source: %{name}-%{version}.tar.gz

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
This package provides a test CA useful to implement functionality and
regression tests for the IGI middleware.

%prep
%setup -c 

%build
# Nothing to build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/grid-security/certificates
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/custom-crls

install -m 644 -p %{name}* $RPM_BUILD_ROOT%{_sysconfdir}/grid-security/certificates
install -m 644 -p *.0 *.r0 *.signing_policy *.namespaces $RPM_BUILD_ROOT%{_sysconfdir}/grid-security/certificates
install -m 644 -p certs/custom-crls/* $RPM_BUILD_ROOT%{_datadir}/%{name}/custom-crls
install -m 644 -p certs/*.pem $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 -p certs/*.p12 $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_sysconfdir}/grid-security/certificates/*
%{_datadir}/%{name}/*

%changelog
* Tue Nov 30 2022 Francesco Giacomini <francesco.giacomini@cnaf.infn.it> - 3.0.3-0
- Add correct CRL

* Tue Nov 29 2022 Enrico Vianello <enrico.vianello at cnaf.infn.it> - 3.0.2-0
- Added revoked certificate and crl + star certificate

* Mon Oct 03 2022 Enrico Vianello <enrico.vianello at cnaf.infn.it> - 3.0.1-0
- Removed old CA

* Mon Oct 03 2022 Enrico Vianello <enrico.vianello at cnaf.infn.it> - 3.0.0-0
- Renew CA and several expired test certificates

* Fri Dec 01 2017 Andrea Ceccanti <andrea.ceccanti at cnaf.infn.it> - 2.0.0-0
- Add new CA certificate for the same CA

* Mon May 05 2014 Andrea Ceccanti <andrea.ceccanti at cnaf.infn.it> - 1.0.6-1
- New certificates.

* Wed Apr 30 2014 Andrea Ceccanti <andrea.ceccanti at cnaf.infn.it> - 1.0.5-1
- New certificates.

* Thu Sep 26 2013 Andrea Ceccanti <andrea.ceccanti at cnaf.infn.it> - 1.0.4-1
- New CRL valid for ten years.

* Tue Sep 17 2013 Andrea Ceccanti <andrea.ceccanti at cnaf.infn.it> - 1.0.3-1
- New certificates for load testing + keystores

* Sun Feb 03 2013 Andrea Ceccanti <andrea.ceccanti at cnaf.infn.it> - 1.0.2-2
- Repackaged custom CRLs to better fit with testsuite

* Fri Feb 01 2013 Andrea Ceccanti <andrea.ceccanti at cnaf.infn.it> - 1.0.2-1
- New custom CRLs that revoke the test0 cert.

* Fri Jan 11 2013 Andrea Ceccanti <andrea.ceccanti at cnaf.infn.it> - 1.0.1-1
- Fixed wrong signing policy files

* Wed Jul 04 2012 Andrea Ceccanti <andrea.ceccanti at cnaf.infn.it> - 1.0.0-1
- Initial release
