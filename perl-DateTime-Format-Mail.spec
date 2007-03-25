#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DateTime
%define	pnam	Format-Mail
Summary:	DateTime::Format::Mail - Convert between DateTime and RFC2822/822 formats
#Summary(pl):
Name:		perl-DateTime-Format-Mail
Version:	0.30
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/D/DR/DROLSKY/DateTime-Format-Mail-%{version}.tar.gz
# Source0-md5:	d3940d6b387b75de0332201db1685e7d
Patch0:		%{name}-datetime_version.patch
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(DateTime)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Params::Validate) >= 0.67
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RFCs 2822 and 822 specify date formats to be used by email. This
module parses and emits such dates.

RFC2822 (April 2001) introduces a slightly different format of date
than that used by RFC822 (August 1982). The main correction is that
the preferred format is more limited, and thus easier to parse
programmatically.

Despite the ease of generating and parsing perfectly valid RFC822 and
RFC2822 people still get it wrong. So this module provides four things
for those handling mail dates:

As a future direction, I'm contemplating an even stricter parser that
will only accept dates with no obsolete elements.



# %description -l pl # TODO

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
%doc AUTHORS Changes CREDITS notes README
%{perl_vendorlib}/DateTime/Format/*.pm
%{_mandir}/man3/*
