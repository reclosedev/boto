%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%define pkgname boto

Summary:        A simple lightweight interface to Amazon Web Services
Name:           python-boto
Version:        2.4.1
Release:        10CROC%{?dist}
License:        MIT
Group:          Development/Languages
URL:            http://github.com/C2Devel/boto
BuildRequires:  python-devel, python-setuptools
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Epoch:          %(date +%s)
Source0:        boto.tar.gz
Provides:       %name = %version-%release

%description
Boto is a Python package that provides interfaces to Amazon Web Services.
It supports S3 (Simple Storage Service), SQS (Simple Queue Service) via
the REST API's provided by those services and EC2 (Elastic Compute Cloud)
via the Query API. The goal of boto is to provide a very simple, easy to
use, lightweight wrapper around the Amazon services.

%prep
%setup -q -n %{pkgname}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README.rst
%{_bindir}/*
%{python_sitelib}/*

%changelog
* Tue Dec 04 2012 Alexey I. Froloff <raorn@altlinux.org> 2.4.1-10
- Revision 2.1.1-755-gf8d9d2a

* Tue Nov 27 2012 Alexey I. Froloff <raorn@altlinux.org> 2.4.1-9
- Revision 98685889e0b138fbbc215109fb197ce6028deafb

* Tue Nov 27 2012 Alexey I. Froloff <raorn@altlinux.org> 2.4.1-8
- Revision 7d947cb5966b1c88e5b434f4260c5ca549f7e7c6

* Tue Oct  2 2012 Stanislav Ievlev <stanislav.ievlev@gmail.com> 2.4.1-7
- Revision 67676f75b9ffc13cc12e7b0ed19472d51ef4ca41

* Tue Oct  2 2012 Ruslan Bayburin <aedeph@gmail.com> 2.4.1-6
- Revision 9fcefb3a3eb4188bcc5066b5332657ce743ca9bd

* Tue Oct  2 2012 Stanislav Ievlev <stanislav.ievlev@gmail.com> 2.4.1-5
- Revision c258d896a705d67de126819b044a3a486205ae7e

* Tue Sep 11 2012 Stanislav Ievlev <stanislav.ievlev@gmail.com> 2.4.1-4
- Revision d33fb0aadf6f548916cddca2871f2dbfd960ac11

* Thu Jul 26 2012 Ruslan Bayburin <aedeph@gmail.com> 2.4.1-3
- Revision dc2c73062ff90fa902b889ce1c5aa57b2906af16

* Thu Jul 26 2012 Dmitry Konishchev <konishchev@gmail.com> 2.4.1-2
- Revision e1cf3da4298305dffc26abd04ae00a74f2fb7f12

* Fri Apr 13 2012 Stanislav Ievlev <stanislav.ievlev@gmail.com> 2.4.1-1
- Revision Next

* Wed Feb 01 2012 Dmitry Konishchev <konishchev@gmail.com> 2.1-2
- Revision 6375bb2c00160e6c73cf5ed22cb2bcf74deed7df

* Fri Aug 19 2011 Nikolay Ivanov <kolya245@gmail.com> 2.0
- Revision 71c2589e47c7b762343f4d51e22c1466478dbcec

* Sat Mar 05 2011 Dmitry Konishchev <konishchev@gmail.com> 2.0b3
- Revision d967d2b9fd4d4455e2ce4a95b0a1980a3066b5a3

