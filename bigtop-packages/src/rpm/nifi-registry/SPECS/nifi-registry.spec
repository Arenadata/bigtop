%define __jar_repack 0

Name:		nifi-registry
Version:	%{nifi_registry_version}
Release:	%{nifi_registry_release}
Summary:	nifi-registry

Group:		Application/Server
License:	Apache License, Version 2.0
URL:		  http://nifi-registry.incubator.apache.org/
Source0:	nifi-registry-%{nifi_registry_version}.tar.gz
Source1:  do-component-build
Source2:  install_nifi-registry.sh
Source3:  nifi-registry.service
Source4: nifi-registry-env.sh
#BIGTOP_PATCH_FILES

BuildArch:  noarch
Requires:	bash
Provides: 	nifi-registry
AutoReqProv: 	no

%description
Apache nifi-registry  is a software project designed to automate the flow of data between software systems.

%prep
%setup -q -n nifi-registry-%{nifi_registry_version}
#BIGTOP_PATCH_COMMANDS

%build
bash %{SOURCE1}

%install
%__rm -rf $RPM_BUILD_ROOT
/bin/bash %{SOURCE2} $RPM_BUILD_ROOT %{nifi_registry_version}
cp -R  %{SOURCE3} $RPM_BUILD_ROOT/usr/lib/systemd/system/
cp -R  %{SOURCE4} $RPM_BUILD_ROOT/usr/lib/nifi-registry/bin/


%pre
getent group nifi >/dev/null || groupadd -r nifi
getent passwd nifi >/dev/null || useradd -c "nifi" -s /sbin/nologin -g nifi -r nifi 2> /dev/null || :

%post
systemctl daemon-reload

%files
%config %attr(0755,nifi,nifi)/etc/nifi-registry
%doc
/usr/lib/systemd/system/*
%attr(0755,nifi,nifi)/usr/lib/nifi-registry
%attr(0755,nifi,nifi)/var/log/nifi-registry

%changelog
