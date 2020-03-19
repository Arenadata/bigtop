%define _binaries_in_noarch_packages_terminate_build 0
%define __jar_repack 0

# This patch should be applied this way only. 
# It can't be applied by common way because pathced file does not exist at prep stage
%define patch0 patch0-change-su-parameters-MON-32.diff

Name: jmxtrans
Version: %{jmxtrans_version}
Release: %{jmxtrans_release}
Summary: JmxTrans
License: (c) 2010 JmxTrans team
Vendor: JmxTrans team
URL: https://github.com/jmxtrans/
Group: Applications/Communications
Packager: JmxTrans team
Requires: java >= 1.7
BuildArch: noarch
Source0:        %{name}-%{jmxtrans_version}.tar.gz
Source1:        do-component-build
Source2:        install_%{name}.sh

%if %{_vendor} == "alt"
%set_verify_elf_method skip
AutoReq: no
%endif



%description
JMX metrics exporter.
This module creates the packaging for JmxTrans. It does not contain any application code, but creates .deb, .rpm
or other packaging.

%prep
%setup

%build
/bin/bash %{SOURCE1}
patch -p1 < %{_sourcedir}/%patch0

%install
/bin/bash %{SOURCE2} --version=%{jmxtrans_version} --prefix=%{buildroot} --build-dir=%{_builddir}

%files
%attr(755,jmxtrans,jmxtrans) /usr/share/jmxtrans/bin
/usr/share/jmxtrans/etc
/usr/share/jmxtrans/lib
/usr/share/jmxtrans/tools
%attr(755,jmxtrans,jmxtrans) /usr/bin/yaml2jmxtrans
%config /etc/jmxtrans 
/etc/init.d/jmxtrans
%dir  /var/lib/jmxtrans
%dir %attr(-,jmxtrans,jmxtrans) /var/log/jmxtrans
%dir %attr(-,jmxtrans,jmxtrans) /var/run/jmxtrans
%exclude /usr/share/jmxtrans/bin/jmxtrans.bat

%pre
if [ $1 = 1 ]; then
  getent group jmxtrans >/dev/null || groupadd -r jmxtrans
  getent passwd jmxtrans >/dev/null || useradd -c "JmxTrans" \
                                               -s /bin/sh -r \
					       -d /usr/share/jmxtrans -g jmxtrans \
						jmxtrans
fi

%post
/sbin/chkconfig --add jmxtrans

%preun
if [ $1 = 0 ]; then
  /sbin/service jmxtrans stop
  /sbin/chkconfig --del jmxtrans
  /usr/sbin/userdel jmxtrans
fi
