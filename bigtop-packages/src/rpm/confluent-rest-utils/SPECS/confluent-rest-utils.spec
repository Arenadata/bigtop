%define __jar_repack 0

Name:		confluent-rest-utils
Version:	%{confluent_rest_utils_version}
Release:	%{confluent_rest_utils_release}
Summary:	confluent-rest-utils

Group:		Applications/Internet
License:	Apache License, Version 2.0
URL:		http://confluent.io
Source0:	confluent-rest-utils-%{confluent_rest_utils_version}.tar.gz
Source1:  do-component-build
Source2:  install_confluent-rest-utils.sh

BuildArch:  noarch
Requires:	bash, confluent-common >= 5.0.0
Provides: 	confluent-rest-utils
AutoReqProv: 	no

%description
Confluent REST Utils provides a small framework and utilities for writing Java REST APIs using Jersey, Jackson, Jetty, and Hibernate Validator.


%prep
%setup -q -n rest-utils-%{confluent_rest_utils_version}

%build
bash %{SOURCE1}

%install
%__rm -rf $RPM_BUILD_ROOT

/bin/bash %{SOURCE2} $RPM_BUILD_ROOT %{confluent_rest_utils_version}

%files
%doc
/usr/share/doc/rest-utils
/usr/share/java/rest-utils


%changelog
