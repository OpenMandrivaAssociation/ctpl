%define use_ccache        	1
%define ccachedir		~/.ccache-OOo%{mdvsuffix}%{?_with_ccache: %global use_ccache 1}%{?_without_ccache: %global use_ccache 0}
%define debug_package          	%{nil}

%define major 2
%define libname %mklibname %{name} %{major}
%define devname %mklibname -d %{name}

Name:		ctpl
Group:		Sciences/Mathematics
License:	GPLv3+
Summary:	Template engine library written in C
Version:	0.3.3
Release:	2
Source:		http://download.tuxfamily.org/ctpl/releases/%{name}-%{version}.tar.gz
URL:		https://ctpl.tuxfamily.org/
BuildRequires:	gtk-doc
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig

%description
CTPL is a template engine library written in C and distributed 
under the terms of the GNU GPLv3+. See the overview in the
documentation for a more complete description.

%package -n %{libname}
Summary: Template engine library written in C
Group:   Sciences/Mathematics

%description -n %{libname}
Library package for ctpl

%package -n %{devname}
Summary: Development files for ctpl
Group:   Sciences/Mathematics

%description -n %{devname}
Development files for ctpl library

%prep
%setup -q

%build
%configure2_5x --enable-gtk-doc -enable-gtk-doc-pdf
%make

%install
%makeinstall

%files
%{_datadir}/gtk-doc/*
%{_datadir}/man/man1/*
%{_bindir}/ctpl

%files -n %{libname}
%{_libdir}/*

%files -n %{devname}
%{_includedir}/%{name}/*

%changelog
* Sun Jul 24 2011 Yuri Myasoedov <omerta13@mandriva.org> 0.2.2-3mdv2012.0
+ Revision: 691420
- Fixed BuildRequires tag for glib2-devel once again
- Fixed release
- Fixed BuildRequires tag for glib2-devel
- Initial package import


