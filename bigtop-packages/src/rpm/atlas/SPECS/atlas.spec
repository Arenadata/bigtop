%define __jar_repack 0

Name:		atlas-metadata
Version:	%{atlas_version}
Release:	%{atlas_release}
Summary:	atlas

Group:		Application/Server
License:	Apache License, Version 2.0
URL:		  http://atlas.incubator.apache.org/
Source0:	apache-atlas-%{atlas_version}-sources.tar.gz
Source1:  do-component-build
Source2:  install_atlas.sh
#Patch0:   ATLAS-2157.patch

BuildArch:  x86_64
Requires:	bash
Provides: 	atlas
AutoReqProv: 	no

%description
Atlas is a scalable and extensible set of core foundational governance services – enabling enterprises to effectively and efficiently meet their compliance requirements within Hadoop and allows integration with the whole enterprise data ecosystem.

%prep
%setup -q -n apache-atlas-sources-%{atlas_version}
#%patch0 -p1

%build
bash %{SOURCE1}

%install
%__rm -rf $RPM_BUILD_ROOT

/bin/bash %{SOURCE2} $RPM_BUILD_ROOT %{atlas_version}

%files
%config /etc/atlas
%doc
/usr/lib/atlas-server

%changelog
