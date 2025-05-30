#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-Module-Util
Version  : 1.09
Release  : 28
URL      : https://cpan.metacpan.org/authors/id/M/MA/MATTLAW/Module-Util-1.09.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MA/MATTLAW/Module-Util-1.09.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libm/libmodule-util-perl/libmodule-util-perl_1.09-3.debian.tar.xz
Summary  : 'Module name tools and transformations'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Module-Util-bin = %{version}-%{release}
Requires: perl-Module-Util-license = %{version}-%{release}
Requires: perl-Module-Util-man = %{version}-%{release}
Requires: perl-Module-Util-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
Module::Util - Module name tools and transformations
SYNOPSIS
use Module::Util qw( :all );

%package bin
Summary: bin components for the perl-Module-Util package.
Group: Binaries
Requires: perl-Module-Util-license = %{version}-%{release}

%description bin
bin components for the perl-Module-Util package.


%package dev
Summary: dev components for the perl-Module-Util package.
Group: Development
Requires: perl-Module-Util-bin = %{version}-%{release}
Provides: perl-Module-Util-devel = %{version}-%{release}
Requires: perl-Module-Util = %{version}-%{release}

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


%package perl
Summary: perl components for the perl-Module-Util package.
Group: Default
Requires: perl-Module-Util = %{version}-%{release}

%description perl
perl components for the perl-Module-Util package.


%prep
%setup -q -n Module-Util-1.09
cd %{_builddir}
tar xf %{_sourcedir}/libmodule-util-perl_1.09-3.debian.tar.xz
cd %{_builddir}/Module-Util-1.09
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Module-Util-1.09/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Module-Util
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Module-Util/a3120e34917d2de1330edbde17f70714d66df81c || :
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

%files bin
%defattr(-,root,root,-)
/usr/bin/pm_which

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Module::Util.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Module-Util/a3120e34917d2de1330edbde17f70714d66df81c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/pm_which.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
