%define		_class		File
%define		_subclass	Fstab
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	2.0.3
Release:	6
Summary:	Read and write fstab files
License:	PHP License
Group:		Development/PHP
URL:		https://pear.php.net/package/File_Fstab/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
File_Fstab is an easy-to-use package which can read & write UNIX fstab
files. It presents a pleasant object-oriented interface to the fstab.
Features:
- Supports blockdev, label, and UUID specification of mount device.
- Extendable to parse non-standard fstab formats by defining a new
  Entry class for that format.
- Easily examine and set mount options for an entry.
- Stable, functional interface.
- Fully documented with PHPDoc.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -f %{buildroot}%{_datadir}/pear/example.php
rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests
rm -rf %{buildroot}%{_datadir}/pear/data

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/example.php
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 2.0.3-3mdv2012.0
+ Revision: 741973
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 2.0.3-2
+ Revision: 679319
- mass rebuild

* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.3-1mdv2011.0
+ Revision: 602138
- new version

* Mon Dec 14 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.2-8mdv2010.1
+ Revision: 478666
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 2.0.2-7mdv2010.0
+ Revision: 441034
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 2.0.2-6mdv2009.0
+ Revision: 236837
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 2.0.2-5mdv2008.1
+ Revision: 136404
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 2.0.2-5mdv2007.0
+ Revision: 81578
- Import php-pear-File_Fstab

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 2.0.2-5mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 2.0.2-4mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 2.0.2-3mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 2.0.2-2mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 2.0.2-1mdk
- 2.0.2

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 2.0.1-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 2.0.1-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 2.0.1-1mdk
- initial Mandriva package (PLD import)

