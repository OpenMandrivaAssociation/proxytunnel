%define	version	1.9.0
%define release %mkrel 6

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


