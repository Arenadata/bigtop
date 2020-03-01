%define         gphome /usr/lib/gpdb
%define         curl curl-7.43.0.tar.gz

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
CURL=%{curl} PREFIX=%{_builddir} /bin/bash %{SOURCE1}
#make clean
#make build-clients
#make PYTHON_VERSION=3 build-clients # this is for building py3client but it needs python37 to be installed
#make CFLAGS="-Wno-unused-variable -Wno-unused-parameter  -Wno-unused-function -Wno-unused-but-set-variable" 

%install

/bin/bash %{SOURCE2} \
          --build-dir=.         \
          --version=%{plcontainer_version} \
          --prefix=%{buildroot}%{gphome} \
          --lib-dir=%{_builddir}

            
#mkdir -p %{buildroot}%{gphome}/share/postgresql/extension
#make install DESTDIR=%{buildroot}%{gphome} bindir=/bin libdir=/lib/postgresql pkglibdir=/lib/postgresql datadir=/share/postgresql
#cp -d /lib64/libjson-c.so* %{buildroot}%{gphome}/lib/
#find /usr/local/lib -xtype f -name "libcurl.so*" | xargs -I{} cp -d {} %{buildroot}%{gphome}/lib/ || exit 1

%files
%defattr(-,root,root)
%{gphome}/lib/postgresql/plcontainer.so
%{gphome}/lib/libjson-c.so
%{gphome}/lib/libjson-c.so.2
%{gphome}/lib/libjson-c.so.2.0.1
%{gphome}/lib/libcurl.so.4.3.0
%{gphome}/lib/libcurl.so.4
%{gphome}/lib/libcurl.so
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

%post
echo "
      Note you should make sure the libcurl
      library path is in the list for library
      lookup. Typically you might want to add
      the path into LD_LIBRARY_PATH and export
      them in shell configuration or greenplum_path.sh
      on all nodes.
      Set this LD_LIBRARY_PATH for plcontainer executables 
      only.
        LD_LIBRARY_PATH=%{gphome}/lib
      (Note you need to restart the Greenplum cluster).
"
      