    %define debug_package %{nil}

Name: gpbackup
Version: %{gpbackup_version}
Release: %{gpbackup_release}
Summary: Greenplum backup
Group: Development/System

Buildroot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
License: ASL 2.0
URL:     https://arenadata.tech/
Source0: gpbackup-%{gpbackup_base_version}.tar.gz
Source1: do-component-build 
Source2: install_%{name}.sh
Source3: bigtop.bom
Source4: gpbackup.sh

Provides: gpbackup
Obsoletes: gptkh
AutoReqProv: no

%description 
gpbackup and gprestore are Go utilities for performing backups and restores of a Greenplum Database.
They are still currently in active development.

%prep
%setup -q -n %{name}-%{gpbackup_base_version}

%build
bash $RPM_SOURCE_DIR/do-component-build

%install
%__rm -rf $RPM_BUILD_ROOT
echo $RPM_BUILD_ROOT
/bin/bash %{SOURCE2} $RPM_BUILD_ROOT %{gpbackup_base_version}
cp -R  %{SOURCE4} $RPM_BUILD_ROOT/etc/profile.d/

# Package file list check

%files 
%attr(0644,root,root)       /etc/profile.d/gpbackup.sh
%dir /usr/lib/gpbackup/bin/
/usr/lib/gpbackup/bin/gpbackup
/usr/lib/gpbackup/bin/gprestore
/usr/lib/gpbackup/bin/gpbackup_helper


# Changelog
#
%changelog
