#
# spec file for package resource-agents
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Since this spec file supports multiple distributions, ensure we
# use the correct group for each.
#
%if 0%{?fedora} || 0%{?centos_version} || 0%{?rhel}
%define pkg_group System Environment/Daemons
%else
%define pkg_group Productivity/Clustering/HA
%endif

%if ! %{defined _rundir}
%define _rundir %{_localstatedir}/run
%endif

Name:           nagios-agents-metadata
Summary:        OCF metadata for nagios agents
License:        LGPL-2.1+ and GPL-2.0+
Group:          %{pkg_group}
Version:        1.0
Release:        0
Url:            https://github.com/ClusterLabs/nagios-agents-metadata
Source:         nagios-agents-metadata-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Provides:       nagios-plugins-metadata
Requires:       monitoring-plugins-fping
Requires:       monitoring-plugins-http
Requires:       monitoring-plugins-ldap
Requires:       monitoring-plugins-mysql
Requires:       monitoring-plugins-pgsql
Requires:       monitoring-plugins-tcp
Requires:       resource-agents

%description
XML files containing metadata which facilitates using nagios
plugins as resource agents. These files were produced from help
pages of individual nagios plugins.

%install
###########################################################
# install nagios plugins XML metadata
tar -xjf %{SOURCE}
mkdir -p %{buildroot}%{_datadir}/nagios/plugins-metadata
for file in $(find plugins-metadata -type f); do
	install -m 644 $file %{buildroot}%{_datadir}/nagios/plugins-metadata
done

###########################################################

%files
###########################################################
%defattr(-,root,root)
%dir %{_datadir}/nagios
%dir %{_datadir}/nagios/plugins-metadata
%attr(0644,root,root) %{_datadir}/nagios/plugins-metadata/*

%changelog
