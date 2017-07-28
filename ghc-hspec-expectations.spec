# generated by cabal-rpm-0.11.1
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name hspec-expectations
%global pkgver %{pkg_name}-%{version}

%bcond_with tests

Name:           ghc-%{pkg_name}
Version:        0.8.2
Release:        1%{?dist}
Summary:        Catchy combinators for HUnit

License:        MIT
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-call-stack-devel
%if %{with tests}
BuildRequires:  ghc-nanospec-devel
%endif
# End cabal-rpm deps

%description
Catchy combinators for HUnit:
<https://github.com/hspec/hspec-expectations#readme>.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development
files.


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


%changelog
* Fri Jul 28 2017 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.8.2-1
- spec file generated by cabal-rpm-0.11.1
