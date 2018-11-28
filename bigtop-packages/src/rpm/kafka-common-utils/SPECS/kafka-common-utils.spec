%define __jar_repack 0

Name:		kafka-common-utils
Version:	%{kafka_common_utils_version}
Release:	%{kafka_common_utils_release}
Summary:	kafka-common-utils

Group:		Applications/Internet
License:	Apache License, Version 2.0
URL:		http://confluent.io
Source0:	kafka-common-utils-%{kafka_common_utils_version}.tar.gz
Source1:  do-component-build
Source2:  install_kafka-common-utils.sh

BuildArch:  noarch
Requires:	bash, kafka
Provides: 	kafka-common-utils
AutoReqProv: 	no

%description
Confluent Common provides shared utilities for Java projects.


%prep
%setup -q -n common-%{kafka_common_utils_version}

%build
bash %{SOURCE1}

%install
%__rm -rf $RPM_BUILD_ROOT

/bin/bash %{SOURCE2} $RPM_BUILD_ROOT %{kafka_common_utils_version}

%files
%doc
/usr/share/doc/kafka-common-utils
/usr/share/java/kafka-common-utils


%changelog
