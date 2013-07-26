%define module  virtinst
%define name    python-%{name}
%define version 0.600.3
%define release 1

Name: 		python-%{module}
Version: 	0.600.4
Release: 	1
Summary:    Python modules for starting Xen guest installations
License:    GPLv2+
Group: 		Development/Python
Url:        http://virt-manager.et.redhat.com/
Source:     https://fedorahosted.org/released/python-virtinst/virtinst-%{version}.tar.gz
BuildRequires:  python-devel
BuildRequires:  python-libvirt
BuildRequires:  python-libxml2
BuildRequires:  python-urlgrabber
BuildArch:      noarch
ExcludeArch:    ppc ppc64 s390 s390x 
Requires:       python-libvirt >= 0.1.4-4
Requires:       python-urlgrabber
Requires:       python-libxml2

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


%changelog
* Fri May 25 2012 Guilherme Moro <guilherme@mandriva.com> 0.600.1-1mdv2012.0
+ Revision: 800571
- Updated to version 0.600.1

* Tue Oct 25 2011 Sergey Zhemoitel <serg@mandriva.org> 0.600.0-1
+ Revision: 707113
- new release 0.600.0

* Wed May 04 2011 Zé <ze@mandriva.org> 0.500.6-1
+ Revision: 665089
- version 0.500.6
- set buildroot and arrange spec

* Sat Feb 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.500.5-1
+ Revision: 636089
- new version
- drop OS patch, merged upstream

  + Bogdano Arendartchuk <bogdano@mandriva.com>
    - added requires for libxml2

* Wed Nov 10 2010 Christiaan Welvaart <spturtle@mandriva.org> 0.500.4-2mdv2011.0
+ Revision: 595646
- rebuild for python 2.7

* Sun Sep 05 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.500.4-1mdv2011.0
+ Revision: 576178
- update to new version 0.500.4

* Mon Mar 29 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.500.3-1mdv2010.1
+ Revision: 528764
- new version

* Tue Feb 09 2010 Frederik Himpe <fhimpe@mandriva.org> 0.500.2-1mdv2010.1
+ Revision: 503324
- Update to new version 0.500.2
- Remove patch integrated upstream

  + Michael Scherer <misc@mandriva.org>
    - fix License
    - add a note about patch, and send it upstream

* Tue Feb 09 2010 Anne Nicolas <ennael@mandriva.org> 0.500.1-2mdv2010.1
+ Revision: 502981
- Add Mandriva in OS list taking into account virtio support

* Tue Dec 15 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.500.1-1mdv2010.1
+ Revision: 478822
- new version

* Sun Oct 11 2009 Frederik Himpe <fhimpe@mandriva.org> 0.500.0-3mdv2010.0
+ Revision: 456603
- Disable Fedora patch which breaks VM creation when there is no
  user qemu

* Wed Oct 07 2009 Frederik Himpe <fhimpe@mandriva.org> 0.500.0-2mdv2010.0
+ Revision: 455687
- Sync patches with Fedora

* Wed Jul 29 2009 Frederik Himpe <fhimpe@mandriva.org> 0.500.0-1mdv2010.0
+ Revision: 404012
- update to new version 0.500.0

* Wed Mar 11 2009 Frederik Himpe <fhimpe@mandriva.org> 0.400.3-1mdv2009.1
+ Revision: 353926
- update to new version 0.400.3

* Sun Mar 08 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.400.2-1mdv2009.1
+ Revision: 353013
- update to new version 0.400.2

* Fri Mar 06 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.400.1-2mdv2009.1
+ Revision: 349839
- rebuild

* Wed Jan 28 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.400.1-1mdv2009.1
+ Revision: 334879
- new version
- drop keyboard patch, merged upstream

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 0.400.0-3mdv2009.1
+ Revision: 323526
- rebuild

* Mon Nov 03 2008 Frederik Himpe <fhimpe@mandriva.org> 0.400.0-2mdv2009.1
+ Revision: 299642
- Add patch from upstream hg repository which fixes parsing of
  Mandriva's /etc/sysconfig/keyboard file

* Mon Oct 13 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.400.0-1mdv2009.1
+ Revision: 293117
- new version

* Thu Aug 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.300.3-1mdv2009.0
+ Revision: 272028
- new version

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.300.1-5mdv2009.0
+ Revision: 259860
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0.300.1-4mdv2009.0
+ Revision: 247708
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Nov 12 2007 Funda Wang <fwang@mandriva.org> 0.300.1-2mdv2008.1
+ Revision: 108178
- rebuild for new lzma

* Fri Nov 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.300.1-1mdv2008.1
+ Revision: 105240
- new version

* Sun Sep 16 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.300.0-1mdv2008.0
+ Revision: 88790
- new version (fix #33395)

* Sat Jun 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.103.0-1mdv2008.0
+ Revision: 34681
- new version


* Fri Feb 23 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.101.0-1mdv2007.0
+ Revision: 125025
- new version

* Wed Dec 13 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.98.0-2mdv2007.1
+ Revision: 96465
- fix dependencies

* Wed Dec 13 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.98.0-1mdv2007.1
+ Revision: 96404
- fix build dependencies
- Import python-virtinst

* Wed Dec 13 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.98.0-1mdv2007.1
- first mdv release


