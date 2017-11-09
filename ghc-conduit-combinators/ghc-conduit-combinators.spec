# generated by cabal-rpm-0.11.1
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name conduit-combinators
%global pkgver %{pkg_name}-%{version}

%bcond_with tests

Name:           ghc-%{pkg_name}
Version:        1.1.1
Release:        2%{?dist}
Summary:        Commonly used conduit functions, for both chunked and unchunked data

License:        MIT
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-base16-bytestring-devel
BuildRequires:  ghc-base64-bytestring-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-chunked-data-devel
BuildRequires:  ghc-conduit-devel
BuildRequires:  ghc-conduit-extra-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-monad-control-devel
BuildRequires:  ghc-mono-traversable-devel
BuildRequires:  ghc-mwc-random-devel
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-resourcet-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-transformers-base-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unix-compat-devel
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-void-devel
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-safe-devel
BuildRequires:  ghc-silently-devel
%endif
# End cabal-rpm deps

%description
Provides a replacement for Data.Conduit.List, as well as a convenient Conduit
module.


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

%package devel-doc
Summary:       Haskell %{pkg_name} library development documentation
BuildArch:     noarch

%description devel-doc
This package provides the Haskell %{pkg_name} development documentation.


%prep
%setup -q -n %{pkgver}


%build
%ghc_lib_build


%install
%ghc_lib_install
grep -v "%{_docdir}/ghc/html/libraries/%{pkgver}" %{name}-devel.files > %{name}-devel-nodoc.files
grep "%{_docdir}/ghc/html/libraries/%{pkgver}" %{name}-devel.files > %{name}-devel-doc.files


%check
%cabal_test


%post devel
%ghc_pkg_recache


%postun devel
%ghc_pkg_recache


%files -f %{name}.files
%license LICENSE


%files devel -f %{name}-devel-nodoc.files
%doc ChangeLog.md README.md

%files devel-doc -f %{name}-devel-doc.files
%doc ChangeLog.md README.md

%changelog
* Thu Nov  9 2017 David Shea <dshea@redhat.com> - 1.1.1-2
- Split documentation into a separate package

* Tue Jul 25 2017 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 1.1.1-1
- spec file generated by cabal-rpm-0.11.1
