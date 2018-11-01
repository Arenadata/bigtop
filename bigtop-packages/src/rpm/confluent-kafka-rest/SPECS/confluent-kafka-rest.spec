%define __jar_repack 0

Name:		confluent-kafka-rest
Version:	%{confluent_kafka_rest_version}
Release:	%{confluent_kafka_rest_release}
Summary:	confluent-kafka-rest

Group:		Applications/Internet
License:	Apache License, Version 2.0
URL:		http://confluent.io
Source0:	confluent-kafka-rest-%{confluent_kafka_rest_version}.tar.gz
Source1:  do-component-build
Source2:  install_confluent-kafka-rest.sh

BuildArch:  noarch
Requires:	bash, confluent-rest-utils
Provides: 	confluent-kafka-rest
AutoReqProv: 	no

%description
A REST proxy for Kafka

%prep
%setup -q -n kafka-rest-%{confluent_kafka_rest_version}

%build
bash %{SOURCE1}

%install
%__rm -rf $RPM_BUILD_ROOT

/bin/bash %{SOURCE2} $RPM_BUILD_ROOT %{confluent_kafka_rest_version}

%files
%doc
/usr/share/doc/kafka-rest
/usr/share/java/kafka-rest
/usr/bin/*
/etc/kafka-rest

%changelog
