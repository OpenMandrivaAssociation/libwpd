%define name		libwpd
%define version		0.8.14
%define release		%mkrel 2
%define api_version	0.8
%define lib_major	8
%define lib_name	%mklibname wpd %{api_version} %{lib_major}
%define develname	%mklibname -d wpd 


Summary:	Library for reading/writing WordPerfect files
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	LGPLv2+
Group:		System/Libraries
URL:		http://libwpd.sourceforge.net/
Source:		http://ovh.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
Patch0:		%{name}-0.8.8-stability.patch
Patch1:		%{name}-0.8.8-typedetect.patch

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	glib2-devel
BuildRequires:	libgsl-devel
BuildRequires:	libgsf-devel
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

%package -n	%{lib_name}
Summary:	Library for reading/writing WordPerfect files
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}
Obsoletes:	%mklibname wpd- 0.8 8

%description -n	%{lib_name}
Libwpd is a library for reading/writing WordPerfect files.
It is designed to be used by another program (e.g.: a word
processor) as an in-process component.
It supports fileimport of all versions of WordPerfect.

%package -n	%{develname}
Summary:	Headers and development files for libwpd
Group:		Development/Other
Requires:	%{lib_name} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{name}-%{api_version}-devel = %{version}-%{release}
Obsoletes:	libwpd0-devel
Obsoletes:	%mklibname -d wpd- 0.8 8

%description -n	%{develname}
Headers and development files for libwpd.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%if %mdkversion < 200900
%post -n %{lib_name} -p /sbin/ldconfig
%endif
 

%if %mdkversion < 200900
%postun -n %{lib_name} -p /sbin/ldconfig
%endif
 

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{name}-tools
%defattr(-,root,root)
%{_bindir}/*

%files -n %{lib_name}
%defattr(-,root,root)
%{_libdir}/libwpd-%{api_version}*.so.*
%{_libdir}/libwpd-stream-%{api_version}*.so.*
%doc CHANGES COPYING INSTALL README TODO

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/pkgconfig/libwpd-%{api_version}.pc
%{_libdir}/pkgconfig/libwpd-stream-%{api_version}.pc
%{_libdir}/libwpd-%{api_version}*.so
%{_libdir}/libwpd-%{api_version}*.la
%{_libdir}/libwpd-stream-%{api_version}*.so
%{_libdir}/libwpd-stream-%{api_version}*.la
%dir %{_includedir}/libwpd-%{api_version}
%dir %{_includedir}/libwpd-%{api_version}/libwpd
%{_includedir}/libwpd-%{api_version}/libwpd/*

%doc %_docdir/libwpd-%{version}/*.png
%doc %_docdir/libwpd-%{version}/html/*.html
%doc %_docdir/libwpd-%{version}/html/*.png
%doc %_docdir/libwpd-%{version}/html/*.css
%doc %_docdir/libwpd-%{version}/CHANGES
%doc %_docdir/libwpd-%{version}/COPYING
%doc %_docdir/libwpd-%{version}/CREDITS
%doc %_docdir/libwpd-%{version}/HACKING
%doc %_docdir/libwpd-%{version}/INSTALL
%doc %_docdir/libwpd-%{version}/README
%doc %_docdir/libwpd-%{version}/TODO
%doc %_docdir/libwpd-%{version}/libwpd.dia


