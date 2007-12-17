%define module	Net-DNS
%define name	perl-%{module}
%define version	0.61
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Perl interface to the DNS resolver
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Net/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl(Digest::HMAC)
BuildRequires:	perl(Net::IP)

%description
Net::DNS is a collection of Perl modules that act as a Domain Name System (DNS)
resolver. It allows the programmer to perform DNS queries that are beyond the
capabilities of gethostbyname and gethostbyaddr.

The programmer should be somewhat familiar with the format of a DNS packet and
its various sections. See RFC 1035 or DNS and BIND (Albitz & Liu) for details.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor < /dev/null
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/*/*
%{perl_vendorarch}/auto/Net
%{perl_vendorarch}/Net

