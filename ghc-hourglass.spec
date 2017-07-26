# generated by cabal-rpm-0.11.1
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name hourglass
%global pkgver %{pkg_name}-%{version}

%bcond_with tests

Name:           ghc-%{pkg_name}
Version:        0.2.10
Release:        1%{?dist}
Summary:        Simple performant time related library

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-deepseq-devel
%if %{with tests}
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-old-locale-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-tasty-quickcheck-devel
BuildRequires:  ghc-time-devel
%endif
# End cabal-rpm deps

%description
Simple time library focusing on simple but powerful and performant API

The backbone of the library are the Timeable and Time type classes.

Each Timeable instances can be converted to type that has a Time instances, and
thus are different representations of current time.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development files.


%prep
%setup -q -n %{pkgver}


%build
%ghc_lib_build


%install
%ghc_lib_install


%check
%cabal_test


%post devel
%ghc_pkg_recache


%postun devel
%ghc_pkg_recache


%files -f %{name}.files
%license LICENSE


%files devel -f %{name}-devel.files
%doc CHANGELOG.md README.md


%changelog
* Wed Jul 26 2017 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.2.10-1
- spec file generated by cabal-rpm-0.11.1
