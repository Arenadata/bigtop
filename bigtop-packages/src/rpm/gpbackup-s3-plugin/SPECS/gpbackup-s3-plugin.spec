    %define debug_package %{nil}

Name: gpbackup-s3-plugin
Version: %{gpbackup_s3_plugin_version}
Release: %{gpbackup_s3_plugin_release}
Summary: Greenplum backup
Group: Development/System

Buildroot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
License: ASL 2.0
URL:     https://arenadata.tech/
Source0: gpbackup-s3-plugin-%{gpbackup_s3_plugin_base_version}.tar.gz
Source1: do-component-build 
Source2: install_%{name}.sh
Source3: bigtop.bom

Requires: gpbackup
Provides: gpbackup-s3-plugin
AutoReqProv: no

%description 
S3 Storage Plugin for gpbackup and gprestore

%prep
%setup -q -n %{name}-%{gpbackup_s3_plugin_base_version}

%build
bash $RPM_SOURCE_DIR/do-component-build

%install
%__rm -rf $RPM_BUILD_ROOT
echo $RPM_BUILD_ROOT
/bin/bash %{SOURCE2} $RPM_BUILD_ROOT %{gpbackup_s3_plugin_base_version}

# Package file list check

%files 
%attr(0644,root,root)    
/usr/lib/gpbackup/bin/gpbackup_s3_plugin




# Changelog
#
%changelog
