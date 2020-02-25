%define debug_package %{nil}

Name: diskquota
Version: %{diskquota_version}
Release: %{diskquota_release}
Summary: Extension that provides disk usage enforcement for database objects in Greenplum DB
Group: Development/Tools

Buildroot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
License: PostgreSQL license
Source0: diskquota-%{diskquota_base_version}.tar.gz
Source1: do-component-build 
Source2: install_%{name}.sh
Source3: bigtop.bom


Requires: bash, gpdb
Provides: diskquota
AutoReqProv: no

%description 
Diskquota is an extension that provides disk usage enforcement for database objects in Greenplum DB

%prep
%setup -q -n %{name}-%{diskquota_base_version}

%build
bash $RPM_SOURCE_DIR/do-component-build

%install
%__rm -rf $RPM_BUILD_ROOT
/bin/bash %{SOURCE2} $RPM_BUILD_ROOT %{diskquota_rest_version}

%pre


%files 
%defattr(-,root,root,755)
/usr/lib/gpdb/lib/postgresql/*
/usr/lib/gpdb/share/postgresql/extension/*
