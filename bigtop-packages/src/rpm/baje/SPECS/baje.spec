%define __jar_repack 0

Name:		baje
Version:	%{baje_version}
Release:	%{baje_release}
Summary:	baje

Group:		Application/Server
License:	arenadata proprietary license
#URL:		  
Source0:	baje-%{baje_version}.tar.gz
Source1:  do-component-build
Source2:  install_baje.sh
Source3:  baje.service
#BIGTOP_PATCH_FILES

BuildArch:  noarch
Requires:	bash
Provides: 	baje
AutoReqProv: 	no

%description
baje

%prep
%setup -q -n baje-%{baje_version}
#BIGTOP_PATCH_COMMANDS

%build
bash %{SOURCE1}

%install
%__rm -rf $RPM_BUILD_ROOT

/bin/bash %{SOURCE2} $RPM_BUILD_ROOT %{baje_version}
%__cp -f %{SOURCE3} $RPM_BUILD_ROOT/usr/lib/systemd/system/

%pre
getent group baje >/dev/null || groupadd -r baje
getent passwd baje >/dev/null || useradd -c "baje" -s /sbin/nologin -g baje -r baje 2> /dev/null || :


%post
systemctl daemon-reload


%files
%config /etc/baje
%attr(0755,root,root)/usr/lib/baje
%attr(0644,root,root)/usr/lib/systemd/system/*
%attr(0755,baje,baje)/var/log/baje

%changelog
