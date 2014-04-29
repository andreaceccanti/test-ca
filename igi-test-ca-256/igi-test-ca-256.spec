Name: igi-test-ca-256
Version: 1.0.0
Release: 2%{?dist}
Summary: A SHA 256 test CA for IGI

Group: Applications/Internet
License: ASL 2.0
URL: https://github.com/andreaceccanti/test-ca

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

install -m 644 -p %{name}.* $RPM_BUILD_ROOT%{_sysconfdir}/grid-security/certificates
install -m 644 -p *.0 *.r0 *.signing_policy *.namespaces $RPM_BUILD_ROOT%{_sysconfdir}/grid-security/certificates
install -m 644 -p certs/*.pem $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 -p certs/*.p12 $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_sysconfdir}/grid-security/certificates/*
%{_datadir}/%{name}/*

%changelog
* Tue Apr 29 2014 Andrea Ceccanti <andrea.ceccanti at cnaf.infn.it> - 1.0.0-2
- Fix namespaces and signing policy files.

* Tue Feb 05 2013 Andrea Ceccanti <andrea.ceccanti at cnaf.infn.it> - 1.0.0-1
- Initial release
