%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif

#python major version
%{expand: %%define pyver %(%{__python} -c 'import sys;print(sys.version[0:3])')}

Name:		python-lazr.authentication
Version:	0.1.2
Release:	1.ius%{?dist}
Summary:	lazr.authentication implements various HTTP authentication 	

Group:		Applicatons/System
License:	GPLv3
URL:		https://launchpad.net/lazr.authentication
Source0:	http://launchpad.net/lazr.authentication/trunk/0.1.2/+download/lazr.authentication-0.1.2.tar.gz
Patch0:		remove_install_requires.diff

BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	noarch

BuildRequires:	python, python-setuptools
Requires:	python
Requires:	python-zope-interface, python-httplib2, python-oauth
Requires:	python-wsgi_intercept

%description
lazr.authentication implements various HTTP authentication schemes as simple pieces of 
WSGI middleware. Currently implemented are HTTP Basic and section 7 of the OAuth specification.

%prep
%setup -q -n lazr.authentication-%{version}
%patch0 -p1

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 \
		    --skip-build \
	     --root %{buildroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc PKG-INFO README.txt HACKING.txt COPYING.txt 
%{python_sitelib}/lazr.authentication-%{version}-py%{pyver}.egg-info/
%{python_sitelib}/lazr.authentication-%{version}-py%{pyver}-nspkg.pth/
%{python_sitelib}/lazr/authentication/


%changelog
* Fri Jun 10 2011 Jeffrey Ness <jeffrey.ness@rackspace.com> - 0.1.2-1.ius
- Initial spec
