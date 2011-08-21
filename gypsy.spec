Name:           gypsy
Version:        0.7
Release:        2%{?dist}
Summary:        A GPS multiplexing daemon

Group:          System Environment/Libraries
# See LICENSE file for details
License:        LGPLv2 and GPLv2
URL:            http://gypsy.freedesktop.org/
Source0:        http://gypsy.freedesktop.org/gypsy-releases/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: bluez-libs-devel
BuildRequires: dbus-devel
BuildRequires: dbus-glib-devel
BuildRequires: glib2-devel
BuildRequires: gtk-doc
BuildRequires: libxslt

# No Bluetooth or USB on those machines
ExcludeArch:   s390 s390x

Requires: dbus

%description
Gypsy is a GPS multiplexing daemon which allows multiple clients to 
access GPS data from multiple GPS sources concurrently. 

%package devel
Summary: Development package for gypsy
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: dbus-glib-devel
Requires: pkgconfig

%description devel
Header files for development with gypsy.

%package docs
Summary: Documentation files for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: gtk-doc
BuildArch: noarch

%description docs
This package contains developer documentation for %{name}.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/libgypsy.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING COPYING.lib LICENSE
%{_sysconfdir}/dbus-1/system.d/Gypsy.conf
%{_datadir}/dbus-1/system-services/org.freedesktop.Gypsy.service
%{_libexecdir}/gypsy-daemon
%{_libdir}/libgypsy.so.0
%{_libdir}/libgypsy.so.0.0.0

%files devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/gypsy.pc
%{_includedir}/gypsy
%{_libdir}/libgypsy.so

%files docs
%defattr(-,root,root,-)
%doc %{_datadir}/gtk-doc/html/gypsy

%changelog
* Tue Jun 01 2010 Bastien Nocera <bnocera@redhat.com> 0.7-2
- Add ExcludeArch for s390
Related: rhbz#595244

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.7-1.1
- Rebuilt for RHEL 6

* Thu Aug 06 2009 Bastien Nocera <bnocera@redhat.com> 0.7-1
- Update to 0.7

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 19 2009 Bastien Nocera <bnocera@redhat.com> 0.6-9
- Gypsy is supposed to run as a system service, as root

* Wed Mar  4 2009 Peter Robinson <pbrobinson@gmail.com> 0.6-8
- Move docs to noarch, some spec file updates

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 18 2008 Peter Robinson <pbrobinson@gmail.com> 0.6-6
- Add gtk-doc build req

* Sat Nov 22 2008 Peter Robinson <pbrobinson@gmail.com> 0.6-5
- Rebuild

* Thu Sep 11 2008 - Bastien Nocera <bnocera@redhat.com> 0.6-4
- Rebuild

* Mon May 15 2008 Peter Robinson <pbrobinson@gmail.com> 0.6-3
- Further spec file cleanups

* Mon Apr 28 2008 Peter Robinson <pbrobinson@gmail.com> 0.6-2
- Some spec file cleanups

* Sat Apr 26 2008 Peter Robinson <pbrobinson@gmail.com> 0.6-1
- Initial package
