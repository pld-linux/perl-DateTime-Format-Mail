#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DateTime
%define	pnam	Format-Mail
Summary:	DateTime::Format::Mail - Convert between DateTime and RFC 2822/822 formats
Summary(pl.UTF-8):	DateTime::Format::Mail - konwersja między formatami DateTime a RFC 2822/822
Name:		perl-DateTime-Format-Mail
Version:	0.3001
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/DateTime/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	15e36249e866463bd0237262a8e43b16
Patch0:		%{name}-datetime_version.patch
URL:		http://search.cpan.org/dist/DateTime-Format-Mail/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-DateTime
BuildRequires:	perl-Params-Validate >= 0.67
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RFCs 2822 and 822 specify date formats to be used by email. This
module parses and emits such dates.

%description -l pl.UTF-8
RFC 2822 i 822 określają formaty daty przeznaczone do używania w
poczcie elektronicznej. Ten moduł analizuje i tworzy takie daty.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS Changes CREDITS README
%{perl_vendorlib}/DateTime/Format/Mail.pm
%{_mandir}/man3/DateTime::Format::Mail.3pm*
