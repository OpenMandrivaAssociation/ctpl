%define name			ctpl
%define version			0.2.2
%define release			1

%define use_ccache        	1
%define ccachedir		~/.ccache-OOo%{mdvsuffix}%{?_with_ccache: %global use_ccache 1}%{?_without_ccache: %global use_ccache 0}
%define _enable_debug_packages 	%{nil}
%define debug_package          	%{nil}

Name:		%{name}
Group:		Sciences/Mathematics
License:	GPLv3+
Summary:	CTPL is a template engine library written in C
Version:	0.2.2
Release:	%mkrel %{release}
Source:		http://download.tuxfamily.org/%{name}/releases/%{name}-%{version}.tar.gz
URL:		http://ctpl.tuxfamily.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	gtk-doc
BuildRequires:	libglib2.0-devel
BuildRequires:	pkgconfig

%description
CTPL is a template engine library written in C and distributed 
under the terms of the GNU GPLv3+. See the overview in the
documentation for a more complete description.

%prep
%setup -q

%build
%configure2_5x --enable-gtk-doc -enable-gtk-doc-pdf
%make

%install
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/gtk-doc/*
%{_datadir}/man/man1/*
%{_bindir}/ctpl
%{_libdir}/*
%{_includedir}/%{name}/*