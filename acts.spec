Name:           acts
Version:        1.4.1
Release:        1%{?dist}
Summary:        Acts is a backup rotation tool for Tarsnap

License:        Unlicense
URL:            https://github.com/alexjurkiewicz/%{name}/
Source0:        https://github.com/alexjurkiewicz/%{name}/archive/v%{version}.tar.gz

Requires:       tarsnap

%description

%global debug_package %{nil}

%prep
%autosetup


%build
rm -r contrib/openbsd 

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/usr/local/bin
install -m 0755 acts $RPM_BUILD_ROOT/usr/local/bin/acts

mkdir -p $RPM_BUILD_ROOT/usr/share/doc/acts
install -m 0600 acts.conf.sample $RPM_BUILD_ROOT/usr/share/doc/acts/acts.conf.sample

cp -r contrib $RPM_BUILD_ROOT/usr/share/doc/acts/contrib
cp LICENSE $RPM_BUILD_ROOT/usr/share/doc/acts/LICENSE


%files
%doc /usr/share/doc/acts
/usr/local/bin/acts



%changelog
* Thu Jun 11 2020 Tyler Griffiths <t@tyjgr.com>
- 
