# generated by cabal-rpm-0.11.1
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name profunctors
%global pkgver %{pkg_name}-%{version}

Name:           ghc-%{pkg_name}
Version:        5.2.1
Release:        3%{?dist}
Summary:        Profunctors

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-base-orphans-devel
BuildRequires:  ghc-bifunctors-devel
BuildRequires:  ghc-comonad-devel
BuildRequires:  ghc-contravariant-devel
BuildRequires:  ghc-distributive-devel
BuildRequires:  ghc-tagged-devel
BuildRequires:  ghc-transformers-devel
# End cabal-rpm deps

%description
Profunctors.


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


%post devel
%ghc_pkg_recache


%postun devel
%ghc_pkg_recache


%files -f %{name}.files
%license LICENSE


%files devel -f %{name}-devel.files
%doc CHANGELOG.markdown README.markdown


%changelog
* Mon Oct 16 2017 David Shea <dshea@redhat.com> - 5.2.1-3
- Rebuild against Fedora comonad

* Tue Sep 12 2017 David Shea <dshea@redhat.com> - 5.2.1-2
- Rebuild against rebuilt dependencies

* Thu Aug  3 2017 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 5.2.1-1
- spec file generated by cabal-rpm-0.11.1
