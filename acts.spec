Name:           acts
Version:        1.4.1
Release:        5%{?dist}
Summary:        A backup rotation tool for Tarsnap

License:        Unlicense
URL:            https://github.com/alexjurkiewicz/%{name}/
Source0:        https://github.com/alexjurkiewicz/%{name}/archive/v%{version}.tar.gz

Patch0:         01-allow-etc-%{name}-%{name}-conf.patch
Patch1:         02-systemd-usr-bin.patch

Requires:       tarsnap

%description

%global debug_package %{nil}

%prep
%autosetup


%build

%install

## Clear any previous builds
rm -rf %{buildroot}

## Create directories
mkdir -p %{buildroot}/%{_sysconfdir}/%{name}
mkdir -p %{buildroot}/usr/share/doc/%{name}
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/etc/systemd/system

## Install binary
install -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}

## Install config example and pre/post scripts
install -m 0600 %{name}.conf.sample %{buildroot}/%{_sysconfdir}/%{name}/%{name}.conf.sample
install -m 0755 contrib/%{name}-pre.sh %{buildroot}/%{_sysconfdir}/%{name}/%{name}-pre.sh
install -m 0755 contrib/%{name}-post.sh %{buildroot}/%{_sysconfdir}/%{name}/%{name}-post.sh

## Install license and documentation
install -m 0644 LICENSE %{buildroot}/%{_docdir}/%{name}/LICENSE
install -m 0644 README.md %{buildroot}/%{_docdir}/%{name}/README.md

## install Systemd units
install -m 0755 contrib/systemd/%{name}.service %{buildroot}/%{_sysconfdir}/systemd/system/%{name}.service
install -m 0755 contrib/systemd/%{name}.timer %{buildroot}/%{_sysconfdir}/systemd/system/%{name}.timer


%files
%license %{_docdir}/%{name}/LICENSE
%doc %{_docdir}/%{name}/README.md
%config %{_sysconfdir}/%{name}/%{name}.conf.sample
%{_sysconfdir}/%{name}/%{name}-pre.sh
%{_sysconfdir}/%{name}/%{name}-post.sh
%{_sysconfdir}/systemd/system/%{name}.service
%{_sysconfdir}/systemd/system/%{name}.timer
%{_bindir}/%{name}



%changelog
* Thu Jun 11 2020 Tyler Griffiths <t@tyjgr.com>
- Move into /usr/bin directory directly.
* Thu Jun 11 2020 Tyler Griffiths <t@tyjgr.com>
- Initial build from upstream
