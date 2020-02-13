%define debug_package %{nil}

Name: madlib-adb6
Version: %{madlib_adb6_version}
Release: %{madlib_adb6_release}
Summary: Apache MADlib for adb 6 is an Open-Source Library for Scalable in-Database Analytics
Group: Development/Libraries

Buildroot: %(mktemp -ud %{_tmppath}/%{madlib_adb6_name}-%{version}-%{release}-XXXXXX)
License: ASL 2.0
Source0: madlib-adb6-%{madlib_adb6_base_version}.tar.gz
Source1: do-component-build 
Source2: install_%{name}.sh
Source3: bigtop.bom
#BIGTOP_PATCH_FILES

Requires: bash, python >= 2.6, m4 >= 1.4
Provides: madlib-adb6
AutoReqProv: no

%description 
Apache MADlib analytics. It provides data-parallel implementations of mathematical,
statistical and machine learning methods for structured and
unstructured data.

The MADlib mission: to foster widespread development of scalable
analytic skills, by harnessing efforts from commercial practice,
academic research, and open-source development.

To more information, please see the MADlib wiki at
https://cwiki.apache.org/confluence/display/MADLIB


%prep
%setup -q -n  madlib-rel-v%{madlib_adb6_base_version}
#BIGTOP_PATCH_COMMANDS
%build
bash $RPM_SOURCE_DIR/do-component-build

%install
%__rm -rf $RPM_BUILD_ROOT
/bin/bash %{SOURCE2} $RPM_BUILD_ROOT %{madlib_adb6_base_version}

%pre


%files 
%defattr(-,root,root,755)
/usr/local/madlib-adb6/*
