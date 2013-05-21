%define upstream_name Net-DNS
%define upstream_version 0.68
%define module Net-DNS

Name:		perl-%{module}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Perl interface to the DNS resolver
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

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
%setup -q -n %{module}-%{upstream_version}
%__rm -f lib/Net/DNS/Resolver/Win32.pm
%__sed -i -e '/Win32.pm/d' MANIFEST

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}"

%check
%__make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/*/*
%{perl_vendorarch}/auto/Net
%{perl_vendorarch}/Net


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.660.0-6mdv2012.0
+ Revision: 765524
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.660.0-5
+ Revision: 764040
- rebuilt for perl-5.14.x

* Thu May 05 2011 Funda Wang <fwang@mandriva.org> 0.660.0-4
+ Revision: 669256
- add br

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 0.660.0-3mdv2011.0
+ Revision: 564568
- rebuild for perl 5.12.1

  + Sandro Cazzaniga <kharec@mandriva.org>
    - rebuild

* Thu Dec 31 2009 Jérôme Quelin <jquelin@mandriva.org> 0.660.0-1mdv2010.1
+ Revision: 484373
- update to 0.66

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.650.0-1mdv2010.0
+ Revision: 404091
- rebuild using %%perl_convert_version

* Sun Mar 15 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.65-2mdv2009.1
+ Revision: 355281
- add ipv6 support

* Thu Jan 29 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.65-1mdv2009.1
+ Revision: 335367
- update to new version 0.65

* Sun Jan 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.64-1mdv2009.1
+ Revision: 324514
- update to new version 0.64

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.63-2mdv2009.0
+ Revision: 223850
- rebuild

* Sat Feb 09 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.63-1mdv2008.1
+ Revision: 164630
- update to new version 0.63

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 0.62-2mdv2008.1
+ Revision: 151278
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sat Dec 29 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.62-1mdv2008.1
+ Revision: 139200
- update to new version 0.62

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.61-1mdv2008.0
+ Revision: 63960
- update to new version 0.61

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.60-1mdv2008.0
+ Revision: 46532
- update to new version 0.60


* Thu Sep 28 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.59-1mdv2007.0
- New version 0.59

* Mon Jul 10 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.58-1mdv2007.0
- New version 0.58

* Wed Mar 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.57-1mdk
- New release 0.57

* Thu Dec 15 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.55-1mdk
- New release 0.55

* Wed Dec 14 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.54-1mdk
- New release 0.54

* Mon Oct 03 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.53-1mdk
- new version
- %%mkrel

* Tue Sep 27 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.52-2mdk
- rpmbuildupate aware
- spec cleanup
- better summary and description
- drop useless requires exception

* Fri Jul 15 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.52-1mdk
- 0.52

* Thu Jun 23 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.51-2mdk
- BuildRequires perl-Net-IP

* Tue Jun 14 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.51-1mdk
- 0.51

* Mon May 02 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.49-1mdk
- 0.49

* Tue Nov 16 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.48-3mdk
- rebuild for new perl

* Mon Aug 30 2004 Christiaan Welvaart <cjw@daneel.dyndns.org> 0.48-2mdk
- add BuildRequires: perl-Digest-HMAC

* Mon Aug 23 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.48-1mdk
- 0.48.
- Add make test.

* Thu Apr 15 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.47-1mdk
- 0.47.

