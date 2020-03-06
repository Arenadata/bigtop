%define __jar_repack 0

# disable debuginfo packages
%define debug_package %{nil}

Name:		clickhouse-jdbc-bridge
Version:	%{clickhouse_jdbc_bridge_version}
Release:	%{clickhouse_jdbc_bridge_release}
Summary:	Yandex ClickHouse DBMS jdbc driver

Group:		Applications/Databases
License:	Apache License, Version 2.0
Vendor: Yandex
Packager: ArenaData
Url: https://clickhouse.yandex/
BuildArch:      noarch

%if %{_vendor} == "alt"
AutoReq: no
Requires(pre): lsb-init
%endif

Source0:	clickhouse-jdbc-bridge-%{clickhouse_jdbc_bridge_version}.tar.gz
Source1:        do-component-build
Source2:        install_clickhouse-jdbc-bridge.sh
Source3:        clickhouse-jdbc-bridge
#BIGTOP_PATCH_FILES

%description
Yandex ClickHouse DBMS jdbc bridge

%prep
%setup -q -n clickhouse-jdbc-bridge-%{clickhouse_jdbc_bridge_version}
#BIGTOP_PATCH_COMMANDS

%build
bash %{SOURCE1} %{clickhouse_jdbc_bridge_version}

%install
%__rm -rf $RPM_BUILD_ROOT 

/bin/bash %{SOURCE2} %{buildroot} %{clickhouse_jdbc_bridge_version}

%post
CHJBUSER="clickhouse-jdbc-bridge"
CHJBGROUP="clickhouse-jdbc-bridge"
getent group "$CHJBGROUP" >/dev/null || groupadd -r "$CHJBGROUP"
getent passwd "$CHJBUSER" >/dev/null || useradd -g "$CHJBGROUP" -c "$CHJBUSER" -d /usr/share/clickhouse-jdbc-bridge -r -M "$CHJBUSER" 2> /dev/null || :

%files
# just include the whole directory
%defattr(-,root,root)
/usr/share/clickhouse-jdbc-bridge
/var/cache/clickhouse-jdbc-bridge
/var/lib/clickhouse-jdbc-bridge
/var/log/clickhouse-jdbc-bridge
/etc/clickhouse-jdbc-bridge
/var/run/clickhouse-jdbc-bridge
/etc/init.d/*


%changelog
