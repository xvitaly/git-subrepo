%global commit0 a7ee886e0260e847dea6240eaa6278fb2f23be8a
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20170206

Name: git-subrepo
Version: 0.3.1
Release: 1.%{date}git%{shortcommit0}%{?dist}

License: MIT
Summary: Git Submodule Alternative
URL: https://github.com/ingydotnet/%{name}
Source0: %{url}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Patch0: git-subrepo-fix-shebangs.patch
BuildArch: noarch

Requires: git-core
BuildRequires: git

%description
This git command "clones" an external git repo into a subdirectory
of your repo. Later on, upstream changes can be pulled in, and local
changes can be pushed back. Simple.

%prep
%autosetup -n %{name}-%{commit0} -p1

%build
# Nothing to build...

%install
%make_install PREFIX=%{_prefix}

%files
%license License
%doc ReadMe.pod Intro.pod Changes
%{_libexecdir}/git-core/%{name}
%{_libexecdir}/git-core/%{name}.d
%{_mandir}/man1/*

%changelog
* Tue Apr 17 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.3.1-1.20170206gita7ee886
- Initial release.