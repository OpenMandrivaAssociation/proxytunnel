%define	version	1.9.0
%define release %mkrel 7

Summary:	Proxytunnel SSH to connect through HTTPS proxies
Name:		proxytunnel
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Communications
Source0:	http://prdownloads.sourceforge.net/proxytunnel/%{name}-%{version}.tar.bz2
URL:		http://proxytunnel.sourceforge.net/
Requires:	ssh-clients
BuildRequires:	openssl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Proxytunnel is a program that connects stdin and stdout to an origin
server somewhere in the Internet through an industry standard HTTPS
proxy. This will allow you for example to access SSH servers when you
normally only have http(s) access.

%prep
%setup -q

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
install %{name} ${RPM_BUILD_ROOT}%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc CHANGES CREDITS LICENSE.txt README
%{_bindir}/*




%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.9.0-7mdv2011.0
+ Revision: 614615
- the mass rebuild of 2010.1 packages

* Tue Apr 13 2010 Funda Wang <fwang@mandriva.org> 1.9.0-6mdv2010.1
+ Revision: 534503
- rebuild

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.9.0-5mdv2010.0
+ Revision: 430809
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 1.9.0-4mdv2009.0
+ Revision: 259320
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.9.0-3mdv2009.0
+ Revision: 247229
- rebuild

* Wed Mar 05 2008 Stefan van der Eijk <stefan@mandriva.org> 1.9.0-1mdv2008.1
+ Revision: 179356
- 1.9.0

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 31 2007 Stefan van der Eijk <stefan@mandriva.org> 1.8.0-1mdv2008.1
+ Revision: 139920
- 1.8.0
- 1.8.0

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Feb 25 2007 Stefan van der Eijk <stefan@mandriva.org> 1.7.0-1mdv2007.0
+ Revision: 125665
- 1.7.0
- Import proxytunnel

* Thu Jun 15 2006 Stefan van der Eijk <stefan@eijk.nu> 1.6.3-1mdk
- New release 1.6.3

* Wed Feb 22 2006 Stefan van der Eijk <stefan@eijk.nu> 1.6.0-1mdk
- 1.6.0

* Wed Aug 17 2005 Stefan van der Eijk <stefan@eijk.nu> 1.5.0-1mdk
- 1.5.0
- %%mkrel

* Mon Nov 29 2004 Stefan van der Eijk <stefan@mandrake.org> 1.2.3-1mdk
- 1.2.3

* Mon Jun 28 2004 Stefan van der Eijk <stefan@mandrake.org> 1.1.3-1mdk
- initial package

