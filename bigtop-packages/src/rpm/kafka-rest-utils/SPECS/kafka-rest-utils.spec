%define __jar_repack 0

Name:		kafka-rest-utils
Version:	%{kafka_rest_utils_version}
Release:	%{kafka_rest_utils_release}
Summary:	kafka-rest-utils

Group:		Applications/Internet
License:	Apache License, Version 2.0
URL:		http://confluent.io
Source0:	kafka-rest-utils-%{kafka_rest_utils_version}.tar.gz
Source1:  do-component-build
Source2:  install_kafka-rest-utils.sh

BuildArch:  noarch
Requires:	bash, kafka-common-utils
Provides: 	kafka-rest-utils
AutoReqProv: 	no

%description
Kafka REST Utils provides a small framework and utilities for writing Java REST APIs using Jersey, Jackson, Jetty, and Hibernate Validator.


%prep
%setup -q -n rest-utils-%{kafka_rest_utils_version}

%build
bash %{SOURCE1}

%install
%__rm -rf $RPM_BUILD_ROOT

/bin/bash %{SOURCE2} $RPM_BUILD_ROOT %{kafka_rest_utils_version}

%files
%doc
/usr/share/doc/rest-utils
/usr/share/java/rest-utils


%changelog
