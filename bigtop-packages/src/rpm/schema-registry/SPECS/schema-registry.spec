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
Source7:  kafka-avro-console-consumer
Source8:  kafka-avro-console-producer
Source9:  schema-registry-start

BuildArch:  noarch
Requires:	bash, kafka-rest-utils = %{schema_registry_version}, schema-registry-kafka-serde-tools = %{schema_registry_version}
Provides: 	schema-registry
AutoReqProv: 	no

%description
RESTful Avro schema registry for Kafka


%package kafka-serde-tools
Summary: kafka-serde-tools
Group: Application/Server
Requires: bash
AutoReq: no

%description kafka-serde-tools
kafka-serde-tools 

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
cp -R  %{SOURCE7} $RPM_BUILD_ROOT/usr/lib/schema-registry/bin/
cp -R  %{SOURCE8} $RPM_BUILD_ROOT/usr/lib/schema-registry/bin/
cp -R  %{SOURCE9} $RPM_BUILD_ROOT/usr/lib/schema-registry/bin/
ln -sf /usr/lib/schema-registry/bin/schema-registry-run-class $RPM_BUILD_ROOT/usr/bin/
ln -sf /usr/lib/schema-registry/bin/kafka-avro-console-consumer $RPM_BUILD_ROOT/usr/bin/
ln -sf /usr/lib/schema-registry/bin/kafka-avro-console-producer $RPM_BUILD_ROOT/usr/bin/

%pre
getent group kafka >/dev/null || groupadd -r kafka
getent passwd schema-registry >/dev/null || useradd -c "schema-registry" -s /sbin/nologin -g kafka -r schema-registry 2> /dev/null || :


%files
%doc
/usr/bin/*
%attr(0755,schema-registry,kafka)/usr/share/doc/schema-registry/*
%attr(0755,schema-registry,kafka)/usr/lib/schema-registry
%attr(0664,root,root)/etc/systemd/system/*
%config(noreplace)/etc/schema-registry

%files kafka-serde-tools
%attr(0755,schema-registry,kafka)/usr/share/doc/kafka-serde-tools/*
%attr(0755,schema-registry,kafka)/usr/share/java/kafka-serde-tools/*


%changelog
