%define libname %mklibname GLw 1
%define devname %mklibname GLw -d

Summary: Xt / Motif OpenGL widgets
Name: libGLw
Version: 7.11.2
Release: 1
License: MIT
Group: System/Libraries
URL: http://www.mesa3d.org
Source0: ftp://ftp.freedesktop.org/pub/mesa/%version/MesaLib-%version.tar.bz2
Patch0: mesa-6.5-build-config.patch
Patch1: mesa-7.11.2-libGLw.patch
BuildRequires: lesstif-devel
BuildRequires: pkgconfig(gl)

%description
Mesa libGLw runtime library.

%package -n %libname
Summary: Xt / Motif OpenGL widgets
Group: System/Libraries

%description -n %libname
Mesa libGLw runtime library.

%package -n %devname
Summary: Mesa libGLw development package
Group: Development/C
Requires: %libname = %version-%release

%description -n %devname
Mesa libGLw development package.

%prep
%setup -q -n Mesa-%{version}

%patch0 -p0 -b .build-config
%patch1 -p1 -b .motif

%build
make OPT_FLAGS="$RPM_OPT_FLAGS" LIB_DIR=%{_lib} linux

%install
rm -rf $RPM_BUILD_ROOT
make install INSTALL_DIR=$RPM_BUILD_ROOT%{_prefix} LIB_DIR=%{_lib}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -n %libname
%defattr(-,root,root,-)
%doc src/glw/README
%_libdir/libGLw.so.1*

%files -n %devname
%defattr(-,root,root,-)
%_libdir/libGLw.so
%_includedir/GL/GLwDrawA.h
%_includedir/GL/GLwDrawAP.h
%_includedir/GL/GLwMDrawA.h
%_includedir/GL/GLwMDrawAP.h
%_libdir/pkgconfig/glw.pc
