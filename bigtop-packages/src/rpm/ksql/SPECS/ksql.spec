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
Source3:  ksql
Source4:  ksql-env.sh
Source5:  ksql-run-class
Source6:  ksql-server-start
Source7:  ksql-stop
Source8:  ksql-server.service


BuildArch:  noarch
Requires:	bash, kafka-rest-utils = %{ksql_version}
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

cp -R  %{SOURCE3} $RPM_BUILD_ROOT/usr/lib/ksql/bin/
cp -R  %{SOURCE4} $RPM_BUILD_ROOT/etc/ksql/
cp -R  %{SOURCE5} $RPM_BUILD_ROOT/usr/lib/ksql/bin/
cp -R  %{SOURCE6} $RPM_BUILD_ROOT/usr/lib/ksql/bin/
cp -R  %{SOURCE7} $RPM_BUILD_ROOT/usr/lib/ksql/bin/
cp -R  %{SOURCE8} $RPM_BUILD_ROOT/usr/lib/systemd/system/
ln -sf /usr/lib/ksql/bin/ksql $RPM_BUILD_ROOT/usr/bin/

%pre
getent group kafka >/dev/null || groupadd -r kafka
getent passwd ksql >/dev/null || useradd -c "ksql" -s /sbin/nologin -g kafka -r ksql 2> /dev/null || :

%files
%doc
%attr(0755,ksql,kafka)/usr/share/doc/ksql
%attr(0755,ksql,kafka)/usr/lib/ksql
%attr(0664,root,root)/usr/lib/systemd/system/*
%config(noreplace)/etc/ksql
/usr/bin/*

%changelog
