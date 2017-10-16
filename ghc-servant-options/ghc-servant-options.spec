# generated by cabal-rpm-0.11.2
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name servant-options
%global pkgver %{pkg_name}-%{version}

Name:           ghc-%{pkg_name}
Version:        0.1.0.0
Release:        2%{?dist}
Summary:        Provide responses to OPTIONS requests for Servant applications

License:        MIT
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-servant-foreign-devel
BuildRequires:  ghc-servant-server-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-wai-devel
# End cabal-rpm deps

%description
Provide responses to OPTIONS requests for Servant applications.


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


%post devel
%ghc_pkg_recache


%postun devel
%ghc_pkg_recache


%files -f %{name}.files
%license LICENSE


%files devel -f %{name}-devel.files
%doc README.md


%changelog
* Mon Oct 16 2017 David Shea <dshea@redhat.com> - 0.1.0.0-2
- Rebuild against Fedora comonad

* Fri Sep 29 2017 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.1.0.0-1
- spec file generated by cabal-rpm-0.11.2
