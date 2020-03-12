Summary: Smart data producer for graphite graphing package
Name: diamond
Version: %{diamond_version}
Release: %{diamond_release}
License: MIT License
Group: Development/Libraries
BuildArch: noarch
Vendor: The Diamond Team <diamond@librelist.com>
Provides: diamond
Url: https://github.com/python-diamond/Diamond

%if %{_vendor} == "alt"
Requires: python python-module-configobj python-module-setuptools
BuildRequires: python python-module-configobj python-module-setuptools
%endif

%if %{_vendor} == "redhat"
Requires: python python-configobj python-setuptools
BuildRequires: python python-configobj python-setuptools
%endif

Source0: %{name}-%{diamond_version}.tar.gz
#BIGTOP_PATCH_FILES

%description
Smart data producer for graphite graphing package

%prep
%setup -n %{name}-%{diamond_version}
#it is just a trick to set the version to be found with git describe
git init . 
touch file
git add file
git -c user.name='bigtop' -c user.email='bigtop@apache.org' commit -m "initial commit"
git -c user.name='bigtop' -c user.email='bigtop@apache.org' tag -a v%{diamond_version} -m "v%{diamond_version}"
#BIGTOP_PATCH_COMMANDS

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --root=%{buildroot} --record=INSTALLED_FILES
%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5 || %{_vendor} == "alt")
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

%pre
getent group diamond > /dev/null || /usr/sbin/groupadd -r diamond
getent passwd diamond > /dev/null || /usr/sbin/useradd -r -g diamond \
       -d /var/lib/diamond -s /sbin/nologin diamond

%post
# add diamond service upon initial install
if test "$1" = "1" ; then
    echo "Adding and activating diamond service"
    if chkconfig --add diamond ; then
        true
    else
        logger -p user.err -s -t %name -- "ERROR: Could not enable diamond service."
        exit 0
    fi
fi

# always restart diamond if it was running
if service diamond status > /dev/null 2>&1; then
    echo "Restarting diamond service because it was running."
    if ! service diamond restart ; then
        logger -p user.err -s -t %name -- "ERROR: Could not restart diamond service."
        exit 0
    fi
fi


%preun
# remove service only on final uninstall
if test "$1" = "0" ; then
    if service diamond status > /dev/null 2>&1 ; then
        if ! service diamond stop ; then
            logger -p user.err -s -t "%{name}" -- "ERROR: Uninstall failed. Not able to stop service."
            exit 0
        fi
    fi
    if chkconfig --del diamond ; then
        echo "Removed diamond service."
    else
        logger -p user.err -s -t "%{name}" -- "ERROR: Uninstall failed. Not able to remove service from services from management system."
        exit 0
    fi
fi


%files -f INSTALLED_FILES
%defattr(-,root,root)
%config(noreplace) /etc/diamond/*
