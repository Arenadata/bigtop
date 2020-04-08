# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# disable repacking jars
%define __os_install_post %{nil}

Name: solr-tools
Version: %{solr_tools_version}
Release: %{solr_tools_release}
Summary: Simple command line tool to generate a password hash for security.json
URL: http://lucene.apache.org/solr
Group: Development/Libraries
BuildArch: noarch
License: ASL 2.0
Source0: solr-tools-%{solr_tools_base_version}-src.tgz
Requires: java

%description 
Simple command line tool to generate a password hash for security.json

%prep
%setup -n solr-tools-%{solr_tools_base_version}

%build
mvn package


%install

%__install -D %{_builddir}/%{name}-%{solr_tools_base_version}/target/%{name}-%{solr_tools_base_version}.jar %{buildroot}/usr/share/%{name}/%{name}-%{solr_tools_base_version}.jar


%files 
%attr(0644,root,root) %{_datarootdir}/%{name}/%{name}-%{solr_tools_base_version}.jar

%post
echo ""
echo "#########################################################################"
echo "# Usage: java -jar %{_datarootdir}/%{name}/%{name}-%{solr_tools_base_version}.jar admin 123 #"
echo "# HZtl83vopLyZfOpGedEQveAwvVdAQ1Ukr6dDJPEfs/w= MTIz                     #"              
echo "#########################################################################"
echo ""
