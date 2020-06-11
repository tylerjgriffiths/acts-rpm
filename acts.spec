Name:           acts
Version:        1.4.1
Release:        1%{?dist}
Summary:        Acts is a backup rotation tool for Tarsnap

License:        Unlicense
URL:            https://github.com/alexjurkiewicz/%{name}/
Source0:        https://github.com/alexjurkiewicz/%{name}/archive/v%{version}.tar.gz

Patch0:         01-allow-etc-acts-acts-conf.patch 
Requires:       tarsnap

%description

%global debug_package %{nil}

%prep
%autosetup


%build

%install

## Clear any previous builds
rm -rf $RPM_BUILD_ROOT

## Create directories
mkdir -p $RPM_BUILD_ROOT/etc/acts/
mkdir -p $RPM_BUILD_ROOT/usr/share/doc/acts
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/etc/systemd/system

## Install binary
install -m 0755 acts $RPM_BUILD_ROOT/usr/local/bin/acts

## Install config example and pre/post scripts
install -m 0600 acts.conf.sample $RPM_BUILD_ROOT/etc/acts/acts.conf.sample
install -m 0755 contrib/acts-pre.sh $RPM_BUILD_ROOT/etc/acts/acts-pre.sh
install -m 0755 contrib/acts-post.sh $RPM_BUILD_ROOT/etc/acts/acts-post.sh

## Install license and documentation
install -m 0644 LICENSE $RPM_BUILD_ROOT/usr/share/doc/acts/LICENSE
install -m 0644 README.md $RPM_BUILD_ROOT/usr/share/doc/acts/README.md

## install Systemd units
install -m 0755 contrib/systemd/acts.service $RPM_BUILD_ROOT/etc/systemd/system/acts.service
install -m 0755 contrib/systemd/acts.timer $RPM_BUILD_ROOT/etc/systemd/system/acts.timer


%files
%license /usr/share/doc/acts/LICENSE
%doc /usr/share/doc/acts/README.md
/etc/acts/acts.conf.sample
/etc/acts/acts-pre.sh
/etc/acts/acts-post.sh
/etc/systemd/system/acts.service
/etc/systemd/system/acts.timer
/usr/local/bin/acts



%changelog
* Thu Jun 11 2020 Tyler Griffiths <t@tyjgr.com>
- 
