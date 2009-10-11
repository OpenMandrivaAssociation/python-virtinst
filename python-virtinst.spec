%define module  virtinst
%define name    python-%{name}
%define version 0.500.0
%define release %mkrel 3

Name: 		python-%{module}
Version: 	%{version}
Release: 	%{release}
Summary:    Python modules for starting Xen guest installations
License:    GPL
Group: 		Development/Python
Url:        http://virt-manager.et.redhat.com/
Source:     http://virt-manager.et.redhat.com/download/sources/virtinst/%{module}-%{version}.tar.gz
# Fedora patches
# Don't erroneously set limit for amount of virtio devices (RH bug #499654)
Patch1: virtinst-0.500.0-virtio-dev-limit.patch
# Don't use virtio for cdrom devices (RH bug #517151)
Patch2: virtinst-0.500.0-virtio-cdrom.patch
# Rawhide/F11 can auto detect keymapping (RH bug #487735)
Patch3: virtinst-0.500.0-no-default-keymap.patch
# Update test suite to verify patches
Patch4: virtinst-0.500.0-update-testsuite.patch
# Don't generate bogus disk driver XML.
Patch5: virtinst-0.500.0-bogus-driver-xml.patch
# Add '--disk format=' for specifying format (qcow2, ...) when provisioning
Patch6: virtinst-0.500.0-disk-format.patch
# Add Fedora12 to os dictionary
Patch7: virtinst-0.500.0-f12-distro.patch
# Don't use usermode net for non-root qemu:///system via virt-install
Patch8: virtinst-0.500.0-nonroot-qemu-net.patch
# Fix cdrom installs where the iso is a storage volume (bug #524109)
Patch9: virtinst-0.500.0-no-iso-driver.patch
# Fix path permissions for kernel/initrd download location (bug #523960)
# Disabled: breaks creation of vm if there's no qemu user
Patch10: virtinst-0.500.0-change-path-perms.patch
# Update translations (bz 493795)
Patch11: virtinst-0.500.0-more-translations.patch
Requires:       python-libvirt >= 0.1.4-4
Requires:       python-urlgrabber
BuildRequires:  python-devel
BuildRequires:  python-libvirt
BuildRequires:  python-libxml2
BuildRequires:  python-urlgrabber
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
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
#%patch10 -p1
%patch11 -p1

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot}
mkdir -p %{buildroot}/%{_sbindir}
mv %{buildroot}/%{_bindir}/virt-install %{buildroot}/%{_sbindir}/virt-install

ln -s virtinst %{buildroot}%{python_sitelib}/xeninst
ln -s virt-install %{buildroot}/%{_sbindir}/xenguest-install

%find_lang virtinst

%clean
rm -rf %{buildroot}

%files -f virtinst.lang
%defattr(-,root,root)
%doc README
%{python_sitelib}/virtinst
%{python_sitelib}/virtconv
%{python_sitelib}/xeninst
%{python_sitelib}/*.egg-info
%{_bindir}/virt-convert
%{_bindir}/virt-clone
%{_bindir}/virt-image
%{_sbindir}/virt-install
%{_sbindir}/xenguest-install
%{_mandir}/man1/virt-convert.1*
%{_mandir}/man1/virt-clone.1*
%{_mandir}/man1/virt-image.1*
%{_mandir}/man1/virt-install.1*
%{_mandir}/man5/virt-image.5*
