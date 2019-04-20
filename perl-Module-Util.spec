#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Module-Util
Version  : 1.09
Release  : 11
URL      : https://cpan.metacpan.org/authors/id/M/MA/MATTLAW/Module-Util-1.09.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MA/MATTLAW/Module-Util-1.09.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libm/libmodule-util-perl/libmodule-util-perl_1.09-3.debian.tar.xz
Summary  : 'Module name tools and transformations'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Module-Util-bin = %{version}-%{release}
Requires: perl-Module-Util-license = %{version}-%{release}
Requires: perl-Module-Util-man = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Module::Util - Module name tools and transformations
SYNOPSIS
use Module::Util qw( :all );

%package bin
Summary: bin components for the perl-Module-Util package.
Group: Binaries
Requires: perl-Module-Util-license = %{version}-%{release}
Requires: perl-Module-Util-man = %{version}-%{release}

%description bin
bin components for the perl-Module-Util package.


%package dev
Summary: dev components for the perl-Module-Util package.
Group: Development
Requires: perl-Module-Util-bin = %{version}-%{release}
Provides: perl-Module-Util-devel = %{version}-%{release}

%description dev
dev components for the perl-Module-Util package.


%package license
Summary: license components for the perl-Module-Util package.
Group: Default

%description license
license components for the perl-Module-Util package.


%package man
Summary: man components for the perl-Module-Util package.
Group: Default

%description man
man components for the perl-Module-Util package.


%prep
%setup -q -n Module-Util-1.09
cd ..
%setup -q -T -D -n Module-Util-1.09 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Module-Util-1.09/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Module-Util
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Module-Util/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/Module/Util.pm

%files bin
%defattr(-,root,root,-)
/usr/bin/pm_which

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Module::Util.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Module-Util/deblicense_copyright

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/pm_which.1
