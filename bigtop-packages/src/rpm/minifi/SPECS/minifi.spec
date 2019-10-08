%define __jar_repack 0

Name:		minifi
Version:	%{minifi_version}
Release:	%{minifi_release}
Summary:	minifi

Group:		Application/Server
License:	Apache License, Version 2.0
URL:		  http://minifi.incubator.apache.org/
Source0:	minifi-%{minifi_version}.tar.gz
Source1:  do-component-build
Source2:  install_minifi.sh
Source3:  minifi.service
Source4:  minifi-c2.service
Source5:  c2.sh
#BIGTOP_PATCH_FILES

BuildArch:  noarch
Requires:	bash
Provides: 	minifi
AutoReqProv: 	no

%description
Apache minifi  is a software project designed to automate the flow of data between software systems.

%package toolkit
Summary: Apache minifi Toolkit 
Group: Application/Server
Requires: bash
AutoReq: no

%description toolkit
Apache minifi Toolkit - command line utilities to setup and support minifi in standalone and clustered environments


%package c2
Summary: Apache minifi Toolkit 
Group: Application/Server
Requires: bash
AutoReq: no

%description c2
Apache minifi C2 - command line utilities to setup and support minifi in standalone and clustered environments


%prep
%setup -q -n minifi-%{minifi_version}
#BIGTOP_PATCH_COMMANDS

%build
bash %{SOURCE1}

%install
%__rm -rf $RPM_BUILD_ROOT
/bin/bash %{SOURCE2} $RPM_BUILD_ROOT %{minifi_version}
cp -R  %{SOURCE3} $RPM_BUILD_ROOT/usr/lib/systemd/system/
cp -R  %{SOURCE4} $RPM_BUILD_ROOT/usr/lib/systemd/system/
cp -R  %{SOURCE5} $RPM_BUILD_ROOT/usr/lib/minifi-c2/bin


%pre
getent group minifi >/dev/null || groupadd -r minifi
getent passwd minifi >/dev/null || useradd -c "minifi" -s /sbin/nologin -g minifi -r minifi 2> /dev/null || :

%post
systemctl daemon-reload

%pre c2
getent group minifi >/dev/null || groupadd -r minifi
getent passwd minifi >/dev/null || useradd -c "minifi" -s /sbin/nologin -g minifi -r minifi 2> /dev/null || :

%post c2
systemctl daemon-reload


%files
%config %attr(0755,minifi,minifi) /etc/minifi
%doc
/usr/lib/systemd/system/minifi.service
%attr(0755,minifi,minifi)/usr/lib/minifi

%files toolkit
%attr(0755,minifi,minifi)/usr/lib/minifi-toolkit

%files c2
%config %attr(0755,minifi,minifi) /etc/minifi-c2
/usr/lib/systemd/system/minifi-c2.service
%attr(0755,minifi,minifi)/usr/lib/minifi-c2

%changelog
