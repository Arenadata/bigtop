%define         gphome /usr/lib/gpdb

Summary:        PL/Container for Greenplum database 
License:        Apache License, Version 2.0
Name:           plcontainer
Version:        %{plcontainer_version}
Release:        %{plcontainer_release}
Group:          Development/Tools
AutoReq:        no
AutoProv:       no
Provides:       plcontainer = %{plcontainer_version}
Source0:        %{name}-%{plcontainer_version}.tar.gz
Source1:        do-component-build
Source2:        install_%{name}.sh
Source3:        bigtop.bom

%description
Provides PL/Container procedural language implementation for the Greenplum Database.

%prep
%setup

%build
PATH=%{gphome}/bin:$PATH PREFIX=%{_builddir} /bin/bash %{SOURCE1}

%install

PATH=%{gphome}/bin:$PATH /bin/bash %{SOURCE2} \
          --build-dir=.         \
          --version=%{plcontainer_version} \
          --prefix=%{buildroot}%{gphome} \
          --lib-dir=%{_builddir}


%files
%defattr(-,root,root)
%{gphome}/lib/postgresql/plcontainer.so
%{gphome}/lib/libjson-c.so
%{gphome}/lib/libjson-c.so.2
%{gphome}/lib/libjson-c.so.2.0.1
%{gphome}/bin/plcontainer
%{gphome}/bin/plcontainer_clients/rclient
%{gphome}/bin/plcontainer_clients/librcall.so
%{gphome}/bin/plcontainer_clients/py3client.sh
%{gphome}/bin/plcontainer_clients/rclient.sh
%{gphome}/bin/plcontainer_clients/pyclient.sh
%{gphome}/bin/plcontainer_clients/pyclient
%{gphome}/share/postgresql/plcontainer/plcontainer_uninstall.sql
%{gphome}/share/postgresql/plcontainer/plcontainer_configuration.xml
%{gphome}/share/postgresql/plcontainer/plcontainer_install.sql
%{gphome}/share/postgresql/extension/plcontainer--1.0.0.sql
%{gphome}/share/postgresql/extension/plcontainer_uninstall.sql
%{gphome}/share/postgresql/extension/plcontainer.control
%{gphome}/share/postgresql/extension/plcontainer_install.sql
%{gphome}/share/postgresql/extension/plcontainer--unpackaged--1.0.0.sql
