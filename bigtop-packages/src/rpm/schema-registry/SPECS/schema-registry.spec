%define __jar_repack 0

Name:		schema-registry
Version:	%{schema_registry_version}
Release:	%{schema_registry_release}
Summary:	schema-registry

Group:		Applications/Internet
License:	Apache License, Version 2.0
URL:		http://confluent.io
Source0:	schema-registry-%{schema_registry_version}.tar.gz
Source1:  do-component-build
Source2:  install_schema-registry.sh
Source3:  schema-registry-env.sh
Source4:  schema-registry-run-class
Source5:  schema-registry.service
Source6:  schema-registry-stop

BuildArch:  noarch
Requires:	bash, kafka-rest-utils
Provides: 	schema-registry
AutoReqProv: 	no

%description
RESTful Avro schema registry for Kafka

%prep
%setup -q -n schema-registry-%{schema_registry_version}

%build
bash %{SOURCE1}

%install
%__rm -rf $RPM_BUILD_ROOT

/bin/bash %{SOURCE2} $RPM_BUILD_ROOT %{schema_registry_version}
cp -R  %{SOURCE3} $RPM_BUILD_ROOT/etc/schema-registry/
cp -R  %{SOURCE4} $RPM_BUILD_ROOT/usr/lib/schema-registry/bin/
cp -R  %{SOURCE5} $RPM_BUILD_ROOT/etc/systemd/system/
cp -R  %{SOURCE6} $RPM_BUILD_ROOT/usr/lib/schema-registry/bin/


%files
%doc
%attr(0755,kafka,kafka)/usr/share/doc/schema-registry
%attr(0755,kafka,kafka)/usr/lib/schema-registry
%attr(0664,root,root)/etc/systemd/system/*
%config(noreplace)/etc/schema-registry


%changelog
