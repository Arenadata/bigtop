%define __jar_repack 0

Name:		kafka-rest
Version:	%{kafka_rest_version}
Release:	%{kafka_rest_release}
Summary:	kafka-rest

Group:		Applications/Internet
License:	Apache License, Version 2.0
URL:		http://confluent.io
Source0:	kafka-rest-%{kafka_rest_version}.tar.gz
Source1:  do-component-build
Source2:  install_kafka-rest.sh
Source3:  kafka-rest-env.sh
Source4:  kafka-rest-run-class
Source5:  kafka-rest.service
Source6:  kafka-rest-stop


BuildArch:  noarch
Requires:	bash, kafka-rest-utils
Provides: 	kafka-rest
AutoReqProv: 	no

%description
A REST proxy for Kafka

%prep
%setup -q -n kafka-rest-%{kafka_rest_version}

%build
bash %{SOURCE1}

%install
%__rm -rf $RPM_BUILD_ROOT

/bin/bash %{SOURCE2} $RPM_BUILD_ROOT %{kafka_rest_version}
cp -R  %{SOURCE3} $RPM_BUILD_ROOT/etc/kafka-rest/
cp -R  %{SOURCE4} $RPM_BUILD_ROOT/usr/lib/kafka-rest/bin/
cp -R  %{SOURCE5} $RPM_BUILD_ROOT/etc/systemd/system/
cp -R  %{SOURCE6} $RPM_BUILD_ROOT/usr/lib/kafka-rest/bin/


%files
%doc
%attr(0755,kafka,kafka)/usr/share/doc/kafka-rest
%attr(0755,kafka,kafka)/usr/lib/kafka-rest
%attr(0664,root,root)/etc/systemd/system/*
%config(noreplace)/etc/kafka-rest

%changelog
