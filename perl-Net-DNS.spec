%define upstream_name	 Net-DNS
%define upstream_version 1.15

%define __noautoreq 'perl\\(Digest::HMAC\\)|perl\\(Digest::MD5\\)|perl\\(Digest::SHA\\)|perl\\(MIME::Base64\\)|perl\\(CONFIG\\)|perl\\(OS_CONF\\)'

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1
Summary:    Perl interface to the DNS resolver
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Digest::HMAC) >= 1.10.0
BuildRequires: perl(Digest::MD5) >= 2.130.0
BuildRequires: perl(Digest::SHA) >= 5.230.0
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(IO::Socket) >= 1.240.0
BuildRequires: perl(MIME::Base64) >= 2.110.0
BuildRequires: perl(Test::More) >= 0.520.0
BuildRequires: perl-devel
BuildArch:     noarch

%description
Net::DNS is a collection of Perl modules that act as a Domain Name System (DNS)
resolver. It allows the programmer to perform DNS queries that are beyond the
capabilities of gethostbyname and gethostbyaddr.

The programmer should be somewhat familiar with the format of a DNS packet and
its various sections. See RFC 1035 or DNS and BIND (Albitz & Liu) for details.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
sed -i '#/usr/local/bin/perl#/usr/bin/perl#' demo/*

%build
perl Makefile.PL INSTALLDIRS=vendor < /dev/null
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes *META.yml README  demo
%{_mandir}/*/*
%{perl_vendorlib}/Net
