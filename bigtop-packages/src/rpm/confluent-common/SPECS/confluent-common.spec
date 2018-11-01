%define __jar_repack 0

Name:		confluent-common
Version:	%{confluent_common_version}
Release:	%{confluent_common_release}
Summary:	confluent-common

Group:		Applications/Internet
License:	Apache License, Version 2.0
URL:		http://confluent.io
Source0:	confluent-common-%{confluent_common_version}.tar.gz
Source1:  do-component-build
Source2:  install_confluent-common.sh

BuildArch:  noarch
Requires:	bash
Provides: 	confluent-common
AutoReqProv: 	no

%description
Confluent Common provides shared utilities for Java projects.


%prep
%setup -q -n common-%{confluent_common_version}

%build
bash %{SOURCE1}

%install
%__rm -rf $RPM_BUILD_ROOT

/bin/bash %{SOURCE2} $RPM_BUILD_ROOT %{confluent_common_version}

%files
%doc
/usr/share/doc/confluent-common
/usr/share/java/confluent-common


%changelog
