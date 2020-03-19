%global __os_install_post %{nil}

Name:           airflow
Version:        %{airflow_version}
Release:        %{airflow_release}
Summary:        Programmatically author, schedule and monitor data pipelines
Group:		Development/Libraries
License:        ASL 2.0
URL:            https://airflow.incubator.apache.org/
BuildRequires:	python-devel mariadb-devel libffi-devel cyrus-sasl-devel gcc-c++ python2-pip
AutoReqProv: 	no
Requires:       python
BuildArch:      noarch
Source0:        apache-%{name}-%{airflow_version}-bin.tar.gz

%description
Airflow is a platform to programmatically author, schedule and monitor workflows.

%prep
%setup -n apache-%{name}-%{airflow_version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --root=%{buildroot} --record=INSTALLED_FILES
%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5 || %{_vendor} == "alt")
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

#%{__mkdir} -p %{buildroot}/usr/share/airflow/bin/
#%{__mkdir} -p %{buildroot}/usr/share/airflow/log/

%{__mkdir} -p %{buildroot}/etc/sysconfig/
%{__mkdir} -p %{buildroot}/etc/tmpfiles.d/
%{__mkdir} -p %{buildroot}/usr/lib/systemd/system/
#%{__mkdir} -p %{buildroot}/usr/bin/
%{__mkdir} -p %{buildroot}/run/airflow/
#%{__mkdir} -p %{buildroot}/etc/logrotate.d/

%{__cp} -rp %{_builddir}/apache-%{name}-%{airflow_version}/scripts/systemd/airflow %{buildroot}/etc/sysconfig/
%{__cp} -rp %{_builddir}/apache-%{name}-%{airflow_version}/scripts/systemd/airflow.conf %{buildroot}/etc/tmpfiles.d/
%{__cp} -rp %{_builddir}/apache-%{name}-%{airflow_version}/scripts/systemd/*.service %{buildroot}/usr/lib/systemd/system/
chmod 644 %{buildroot}/usr/lib/systemd/system/*

#%{__cp} -rp %{_topdir}/bin/airflow %{buildroot}/usr/share/airflow/bin/
#%{__cp} -rp %{_topdir}/bin/airflow.bash %{buildroot}/usr/bin/airflow

#%{__cp} -rp %{_topdir}/bin/gunicorn %{buildroot}/usr/share/airflow/bin/
#%{__cp} -rp %{_topdir}/bin/gunicorn.bash %{buildroot}/usr/bin/gunicorn

#%{__cp} -rp %{_topdir}/logrotate/* %{buildroot}/etc/logrotate.d/

%pre
if ! /usr/bin/id airflow &>/dev/null; then
    /usr/sbin/useradd -r -d /usr/share/airflow -s /bin/nologin -c "airflow" airflow|| \
        %logmsg "Unexpected error adding user \"airflow\". Aborting installation."
fi

%post
systemctl daemon-reload

%preun
systemctl stop airflow-flower
systemctl stop airflow-kerberos
systemctl stop airflow-scheduler
systemctl stop airflow-webserver
systemctl stop airflow-worker

%postun
systemctl daemon-reload
if [ $1 -eq 0 ]; then
	/usr/sbin/userdel airflow || %logmsg "User \"airflow\" could not be deleted."
fi

%clean
%{__rm} -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,airflow,airflow,-)
#/usr/share/airflow/
/run/airflow/

%defattr(-,root,root,-)
/etc/sysconfig/*
/etc/tmpfiles.d/*
/usr/lib/systemd/system/*
#/etc/logrotate.d/*

%changelog
