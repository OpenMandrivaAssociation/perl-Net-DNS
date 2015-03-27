%define modname	Net-DNS
%define modver 0.83

Summary:	Perl interface to the DNS resolver

Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Net/%{modname}-%{modver}.tar.gz
BuildRequires:	perl(Digest::HMAC)
BuildRequires:	perl(Net::IP)
BuildRequires:	perl(Digest::SHA)
BuildRequires:	perl(IO::Socket::INET6)
BuildRequires:	perl(Socket6)
BuildRequires:	perl-devel

%description
Net::DNS is a collection of Perl modules that act as a Domain Name System (DNS)
resolver. It allows the programmer to perform DNS queries that are beyond the
capabilities of gethostbyname and gethostbyaddr.

The programmer should be somewhat familiar with the format of a DNS packet and
its various sections. See RFC 1035 or DNS and BIND (Albitz & Liu) for details.

%prep
%setup -qn %{modname}-%{modver}
rm -f lib/Net/DNS/Resolver/MSWin32.pm
sed -i -e '/MSWin32.pm/d' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}"

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorarch}/auto/Net
%{perl_vendorarch}/Net
%{_mandir}/man3/*
