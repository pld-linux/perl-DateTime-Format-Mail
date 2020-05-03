#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	DateTime
%define	pnam	Format-Mail
Summary:	DateTime::Format::Mail - Convert between DateTime and RFC 2822/822 formats
Summary(pl.UTF-8):	DateTime::Format::Mail - konwersja między formatami DateTime a RFC 2822/822
Name:		perl-DateTime-Format-Mail
Version:	0.403
Release:	1
Epoch:		1
# same as perl 5
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/DateTime/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b34a52d96290c42cf53e8db0a8f16ecd
URL:		https://metacpan.org/release/DateTime-Format-Mail
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-DateTime >= 1.04
BuildRequires:	perl-Params-Validate >= 0.67
BuildRequires:	perl-Test-Simple
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

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes CREDITS README
%{perl_vendorlib}/DateTime/Format/Mail.pm
%{_mandir}/man3/DateTime::Format::Mail.3pm*
