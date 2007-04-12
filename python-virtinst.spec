%define module  virtinst
%define name    python-%{name}
%define version 0.101.0
%define release %mkrel 1

Name: 		python-%{module}
Version: 	%{version}
Release: 	%{release}
Summary:    Python modules for starting Xen guest installations
License:    GPL
Group: 		Development/Python
Url:        http://hg.et.redhat.com/virt/applications/xeninst--devel
Source:     %{module}-%{version}.tar.bz2
Requires:       python-libvirt >= 0.1.4-4
Requires:       python-urlgrabber
BuildRequires:  python-devel
BuildArch:      noarch
ExcludeArch:    ppc ppc64 s390 s390x 
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
virtinst is a module to help in starting installations of Fedora/Red
Hat Enterprise Linux related distributions inside of virtual machines.  It
supports both paravirt guests (for which only FC and RHEL guests are
currently supported) as well as fully virtualized guests.  It uses
libvirt (http://www.libvirt.org) for starting things.

Also contained is a simple script virt-install which uses
virtinst in a command line mode.

%prep
%setup -q -n %{module}-%{version} 

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot}
mkdir -p %{buildroot}/%{_sbindir}
mv %{buildroot}/%{_bindir}/virt-install %{buildroot}/%{_sbindir}/virt-install

ln -s virtinst %{buildroot}%{python_sitelib}/xeninst
ln -s virt-install %{buildroot}/%{_sbindir}/xenguest-install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{python_sitelib}/virtinst
%{python_sitelib}/xeninst
%{python_sitelib}/*.egg-info
%{_sbindir}/virt-install
%{_sbindir}/xenguest-install


