%define         postgishome /usr/lib/gpdb
%define         postgis_dir %{_builddir}/%{name}-%{postgis_adb6_version}/postgis/build/postgis-%{postgis_adb6_version}
#%define         postgis_rel %{getenv:project_id}
%define         geos_ver 3.6.0
%define         proj_ver 4.8.0
%define         json_ver 0.12
%define         gdal_ver 2.0.2

Summary:        Geospatial extensions for Greenplum Database
License:        GPLv2
Name:           postgis-adb6
Version:        %{postgis_adb6_version}
Release:        %{postgis_adb6_release}
Group:          Development/Tools
AutoReq:        no
AutoProv:       no
Provides:       postgis = %{postgis_adb6_version}
Obsoletes:      postgis
Requires:       libgeos = %{geos_ver}, libproj = %{proj_ver}, libjson-c = %{json_ver}, libgdal = %{gdal_ver}
Source0:        %{name}-%{postgis_adb6_version}.tar.gz
#Source1:        do-component-build
#Source2:        install_postgis.sh

%description
The PostGIS module provides geospatial extensions for Greenplum Database.

%prep
%setup -q -n %{name}-%{postgis_adb6_version}

%build
cd %{postgis_dir}
%configure --with-pgconfig=/usr/lib/gpdb/bin/pg_config \
           --with-projdir=/usr/include/ \
           --with-gdalconfig=/usr/bin/gdal-config \
           --libdir=%{postgishome}/lib \
           --includedir=%{postgishome}/include

%install

GPHOME=%{buildroot}%{postgishome}

mkdir -p %{buildroot}%{postgishome}/bin \
         %{buildroot}%{postgishome}/lib/postgresql \
         %{buildroot}%{postgishome}/share/postgresql/extension \
         %{buildroot}%{postgishome}/share/postgresql/contrib/postgis-2.1/{install,upgrade,uninstall}/

make %{?_smp_mflags} -C %{postgis_dir} BLD_TOP=%{bld_top} all install DESTDIR=%{buildroot}

cp %{postgis_dir}/extensions/postgis/postgis.control                               %{buildroot}%{postgishome}/share/postgresql/extension/postgis.control
cp %{postgis_dir}/extensions/postgis_topology/postgis_topology.control             %{buildroot}%{postgishome}/share/postgresql/extension/postgis_topology.control
cp %{postgis_dir}/extensions/postgis_tiger_geocoder/postgis_tiger_geocoder.control %{buildroot}%{postgishome}/share/postgresql/extension/postgis_tiger_geocoder.control

#cp ${GPHOME}/bin/pgsql2shp    %{buildroot}%{postgishome}/bin
#cp ${GPHOME}/bin/shp2pgsql    %{buildroot}%{postgishome}/bin
#cp ${GPHOME}/bin/raster2pgsql %{buildroot}%{postgishome}/bin

#cp ${GPHOME}/lib/postgresql/postgis-2.1.so   %{buildroot}%{postgishome}/lib/postgresql/postgis-2.1.so
#cp ${GPHOME}/lib/postgresql/rtpostgis-2.1.so %{buildroot}%{postgishome}/lib/postgresql/rtpostgis-2.1.so


# All the .sql files once installed will be installed in share/contrib/postgis-2.1 folder of your PostgreSQL install

# cp ${GPHOME}/share/postgresql/contrib/postgis-2.1/*.sql %{buildroot}%{postgishome}/share/postgresql/contrib/postgis-2.1/
cp $GPHOME/share/postgresql/contrib/postgis-2.1/postgis.sql %{buildroot}%{postgishome}/share/postgresql/contrib/postgis-2.1/install/
cp $GPHOME/share/postgresql/contrib/postgis-2.1/rtpostgis.sql %{buildroot}%{postgishome}/share/postgresql/contrib/postgis-2.1/install/
cp $GPHOME/share/postgresql/contrib/postgis-2.1/*comments.sql %{buildroot}%{postgishome}/share/postgresql/contrib/postgis-2.1/install/
cp $GPHOME/share/postgresql/contrib/postgis-2.1/spatial_ref_sys.sql %{buildroot}%{postgishome}/share/postgresql/contrib/postgis-2.1/install/


cp $GPHOME/share/postgresql/contrib/postgis-2.1/*upgrade*.sql %{buildroot}%{postgishome}/share/postgresql/contrib/postgis-2.1/upgrade/
cp $GPHOME/share/postgresql/contrib/postgis-2.1/legacy*.sql %{buildroot}%{postgishome}/share/postgresql/contrib/postgis-2.1/upgrade/
cp $GPHOME/share/postgresql/contrib/postgis-2.1/rtpostgis_legacy.sql %{buildroot}%{postgishome}/share/postgresql/contrib/postgis-2.1/upgrade/

cp $GPHOME/share/postgresql/contrib/postgis-2.1/uninstall*.sql %{buildroot}%{postgishome}/share/postgresql/contrib/postgis-2.1/uninstall/

# cp %{postgishome}/share/postgresql/contrib/postgis-2.1/postgis.sql  %{buildroot}%{postgishome}/share/postgresql/extension/postgis--2.1.5.sql
# cp %{postgishome}/share/postgresql/contrib/postgis-2.1/topology.sql %{buildroot}%{postgishome}/share/postgresql/extension/postgis_topology--2.1.5.sql

cp %{postgis_dir}/../../package/postgis_manager.sh %{buildroot}%{postgishome}/share/postgresql/contrib/postgis-2.1/postgis_manager.sh

rm -rf %{buildroot}%{postgishome}/share/postgresql/contrib/postgis-2.1/*.sql
rm -rf %{buildroot}%{postgishome}/share/postgresql/extension/*.sql
rm -f %{buildroot}%{postgishome}/share/postgresql/contrib/postgis-2.1/postgis_restore.pl

%files

%{postgishome}/bin/pgsql2shp
%{postgishome}/bin/raster2pgsql
%{postgishome}/bin/shp2pgsql
%{postgishome}/include/liblwgeom.h
%{postgishome}/lib/liblwgeom-2.1.5.so
%{postgishome}/lib/liblwgeom.a
%{postgishome}/lib/liblwgeom.la
%{postgishome}/lib/liblwgeom.so
%{postgishome}/lib/postgresql/postgis-2.1.so
%{postgishome}/lib/postgresql/rtpostgis-2.1.so

# %{postgishome}/share/postgresql/contrib/postgis-2.1/*
# %{postgishome}/share/postgresql/extension/postgis--2.1.5.sql
# %{postgishome}/share/postgresql/extension/postgis_topology--2.1.5.sql
%{postgishome}/share/postgresql/contrib/postgis-2.1/postgis_manager.sh
%{postgishome}/share/postgresql/contrib/postgis-2.1/install/postgis.sql
%{postgishome}/share/postgresql/contrib/postgis-2.1/install/postgis_comments.sql
%{postgishome}/share/postgresql/contrib/postgis-2.1/install/raster_comments.sql
%{postgishome}/share/postgresql/contrib/postgis-2.1/install/rtpostgis.sql
%{postgishome}/share/postgresql/contrib/postgis-2.1/install/spatial_ref_sys.sql
%{postgishome}/share/postgresql/contrib/postgis-2.1/install/topology_comments.sql
%{postgishome}/share/postgresql/contrib/postgis-2.1/uninstall/uninstall_legacy.sql
%{postgishome}/share/postgresql/contrib/postgis-2.1/uninstall/uninstall_postgis.sql
%{postgishome}/share/postgresql/contrib/postgis-2.1/uninstall/uninstall_rtpostgis.sql
%{postgishome}/share/postgresql/contrib/postgis-2.1/uninstall/uninstall_sfcgal.sql
%{postgishome}/share/postgresql/contrib/postgis-2.1/uninstall/uninstall_topology.sql
%{postgishome}/share/postgresql/contrib/postgis-2.1/upgrade/legacy.sql
%{postgishome}/share/postgresql/contrib/postgis-2.1/upgrade/legacy_gist.sql
%{postgishome}/share/postgresql/contrib/postgis-2.1/upgrade/legacy_minimal.sql
%{postgishome}/share/postgresql/contrib/postgis-2.1/upgrade/postgis_upgrade_20_21.sql
%{postgishome}/share/postgresql/contrib/postgis-2.1/upgrade/postgis_upgrade_21_minor.sql
%{postgishome}/share/postgresql/contrib/postgis-2.1/upgrade/rtpostgis_legacy.sql
%{postgishome}/share/postgresql/contrib/postgis-2.1/upgrade/rtpostgis_upgrade_20_21.sql
%{postgishome}/share/postgresql/contrib/postgis-2.1/upgrade/rtpostgis_upgrade_21_minor.sql
%{postgishome}/share/postgresql/contrib/postgis-2.1/upgrade/topology_upgrade_21_minor.sql

%{postgishome}/share/postgresql/extension/postgis.control
%{postgishome}/share/postgresql/extension/postgis_topology.control
%{postgishome}/share/postgresql/extension/postgis_tiger_geocoder.control
