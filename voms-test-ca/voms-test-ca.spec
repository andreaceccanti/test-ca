Name: voms-test-ca
Version: 1.0.0
Release: 1%{?dist}
Summary: A test CA for VOMS

Group: Applications/Internet
License: ASL 2.0
URL: https://twiki.cnaf.infn.it/twiki/bin/view/VOMS

Source: %{name}-%{version}.tar.gz

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
The Virtual Organization Membership Service (VOMS) is an attribute authority
which serves as central repository for VO user authorization information,
providing support for sorting users into group hierarchies, keeping track of
their roles and other attributes in order to issue trusted attribute
certificates and SAML assertions used in the Grid environment for 
authorization purposes.

This package provides a test CA useful to implement functionality and
regression tests.

%prep
%setup -c 

%build
# Nothing to build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/grid-security/certificates
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}

install -m 644 -p voms-test-ca.* $RPM_BUILD_ROOT%{_sysconfdir}/grid-security/certificates
install -m 644 -p *.0 *.r0 *.signing_policy $RPM_BUILD_ROOT%{_sysconfdir}/grid-security/certificates
install -m 644 -p certs/* $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_sysconfdir}/grid-security/certificates/*
%{_datadir}/%{name}/*

%changelog

* Wed Jul 04 2012 Andrea Ceccanti <andrea.ceccanti at cnaf.infn.it> - 1.0.0-1
- Initial release
