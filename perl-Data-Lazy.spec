#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Data
%define	pnam	Lazy
Summary:	Data::Lazy.pm - "lazy" (defered/on-demand) variables
Summary(pl.UTF-8):	Data::Lazy.pm - zmienne "leniwe" (opóźnione/na żądanie)
Name:		perl-Data-Lazy
Version:	0.6
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/S/SA/SAMV/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	12af27598b4b02300768567e614677a7
URL:		http://search.cpan.org/dist/Data-Lazy/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A very little module for generic on-demand computation of values in a
scalar, array or hash.

It provides scalars that are "lazy", that is their value is computed
only when accessed, and at most once.

%description -l pl.UTF-8
Bardzo mały moduł do ogólnego obliczania na żądanie zmiennych w typie
skalarnym, tablicowym lub haszu.

Udostępnia skalary "leniwe", czyli takie, których wartość jest
obliczana dopiero przy dostępie i najwyżej raz.

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
%doc Changes
%{perl_vendorlib}/Data/*.pm
%{_mandir}/man3/*
