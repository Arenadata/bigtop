%define __jar_repack 0

Name:		confluent-schema-registry
Version:	%{confluent_schema_registry_version}
Release:	%{confluent_schema_registry_release}
Summary:	confluent-schema-registry

Group:		Applications/Internet
License:	Apache License, Version 2.0
URL:		http://confluent.io
Source0:	confluent-schema-registry-%{confluent_schema_registry_version}.tar.gz
Source1:  do-component-build
Source2:  install_confluent-schema-registry.sh

BuildArch:  noarch
Requires:	bash, confluent-rest-utils
Provides: 	confluent-schema-registry
AutoReqProv: 	no

%description
RESTful Avro schema registry for Kafka

%prep
%setup -q -n schema-registry-%{confluent_schema_registry_version}

%build
bash %{SOURCE1}

%install
%__rm -rf $RPM_BUILD_ROOT

/bin/bash %{SOURCE2} $RPM_BUILD_ROOT %{confluent_schema_registry_version}

%files
%doc
/usr/share/doc/schema-registry
/usr/share/java/schema-registry
/usr/bin/*
/etc/schema-registry

%changelog
