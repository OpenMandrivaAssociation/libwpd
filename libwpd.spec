%define api 0.10
%define major 10
%define libname %mklibname wpd %{api} %{major}
%define devname %mklibname -d wpd 

Summary:	Library for reading/writing WordPerfect files
Name:		libwpd
Version:	0.10.3
Release:	5
License:	LGPLv2+
Group:		System/Libraries
Url:		https://libwpd.sourceforge.net/
Source0:	http://dev-www.libreoffice.org/src/%{name}-%{version}.tar.xz
Patch0:		https://src.fedoraproject.org/rpms/libwpd/raw/rawhide/f/libwpd-gcc11.patch
BuildRequires:	doxygen
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(librevenge-0.0)

%description
Libwpd is a library for reading/writing WordPerfect files.
It is designed to be used by another program (e.g.: a word
processor) as an in-process component.
It supports fileimport of all versions of WordPerfect.

%package -n %{name}-tools
Summary:	Tools to transform Wordperfect files to html or text
Group:		Office

%description -n %{name}-tools
Tools to transform Wordperfect files to html or text.
It supports fileimport of all versions of WordPerfect.

%package -n %{libname}
Summary:	Library for reading/writing WordPerfect files
Group:		System/Libraries

%description -n %{libname}
Libwpd is a library for reading/writing WordPerfect files.
It is designed to be used by another program (e.g.: a word
processor) as an in-process component.
It supports fileimport of all versions of WordPerfect.

%package -n %{devname}
Summary:	Headers and development files for libwpd
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Headers and development files for libwpd.

%prep
%autosetup -p1

%build
%ifnarch %{riscv}
CFLAGS="%{optflags} -Qunused-arguments" \
CXXFLAGS="%{optflags} -Qunused-arguments" \
%endif
%configure
%make_build

%install
%make_install

%files -n %{name}-tools
%doc ChangeLog INSTALL README TODO
%{_bindir}/*

%files -n %{libname}
%{_libdir}/libwpd-%{api}.so.%{major}*

%files -n %{devname}
%{_libdir}/pkgconfig/libwpd-%{api}.pc
%{_libdir}/libwpd-%{api}.so
%{_includedir}/libwpd-%{api}
%doc %{_datadir}/doc/libwpd
