%define __jar_repack 0

Name:		ksql
Version:	%{ksql_version}
Release:	%{ksql_release}
Summary:	ksql

Group:		Applications/Internet
License:	Apache License, Version 2.0
URL:		http://confluent.io
Source0:	ksql-%{ksql_version}.tar.gz
Source1:  do-component-build
Source2:  install_ksql.sh


BuildArch:  noarch
Requires:	bash, kafka-rest-utils
Provides: 	ksql
AutoReqProv: 	no

%description
Streaming SQL for Apache Kafka

%prep
%setup -q -n ksql-%{ksql_version}

%build
bash %{SOURCE1}

%install
%__rm -rf $RPM_BUILD_ROOT

/bin/bash %{SOURCE2} $RPM_BUILD_ROOT %{ksql_version}

%files
%doc
%attr(0755,kafka,kafka)/usr/share/doc/ksql
%attr(0755,kafka,kafka)/usr/lib/ksql
#%attr(0664,root,root)/etc/systemd/system/*
%config(noreplace)/etc/ksql

%changelog
