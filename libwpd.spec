%define api	0.9
%define major	9
%define libname %mklibname wpd %{api} %{major}
%define libstream %mklibname wpd-stream %{api} %{major}
%define devname	%mklibname -d wpd 

Summary:	Library for reading/writing WordPerfect files
Name:		libwpd
Version:	0.9.9
Release:	4
License:	LGPLv2+
Group:		System/Libraries
Url:		http://libwpd.sourceforge.net/
Source0:	http://ovh.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz

BuildRequires:	doxygen

%description
Libwpd is a library for reading/writing WordPerfect files.
It is designed to be used by another program (e.g.: a word
processor) as an in-process component.
It supports fileimport of all versions of WordPerfect.

%package -n	%{name}-tools
Summary:	Tools to transform Wordperfect files to html or text
Group:		Office

%description -n %{name}-tools
Tools to transform Wordperfect files to html or text.
It supports fileimport of all versions of WordPerfect.

%package -n	%{libname}
Summary:	Library for reading/writing WordPerfect files
Group:		System/Libraries

%description -n	%{libname}
Libwpd is a library for reading/writing WordPerfect files.
It is designed to be used by another program (e.g.: a word
processor) as an in-process component.
It supports fileimport of all versions of WordPerfect.

%package -n	%{libstream}
Summary:	Library for reading/writing WordPerfect files
Group:		System/Libraries
Conflicts:	%{_lib}wpd0.9_9 < 0.9.2-1

%description -n	%{libstream}
This package contains the library wpd-stream for %{name}.

%package -n	%{devname}
Summary:	Headers and development files for libwpd
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libstream} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
Headers and development files for libwpd.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

%files -n %{name}-tools
%doc ChangeLog INSTALL README TODO
%{_bindir}/*

%files -n %{libname}
%{_libdir}/libwpd-%{api}.so.%{major}*

%files -n %{libstream}
%{_libdir}/libwpd-stream-%{api}.so.%{major}*

%files -n %{devname}
%{_libdir}/pkgconfig/libwpd-%{api}.pc
%{_libdir}/pkgconfig/libwpd-stream-%{api}.pc
%{_libdir}/libwpd-%{api}.so
%{_libdir}/libwpd-stream-%{api}.so
%{_includedir}/libwpd-%{api}
%doc %{_datadir}/doc/libwpd

