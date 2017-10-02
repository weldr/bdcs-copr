# generated by cabal-rpm-0.11.2
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name http-media
%global pkgver %{pkg_name}-%{version}

%bcond_with tests

Name:           ghc-%{pkg_name}
Version:        0.7.1.1
Release:        1%{?dist}
Summary:        Processing HTTP Content-Type and Accept headers

License:        MIT
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-case-insensitive-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-utf8-string-devel
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-test-framework-devel
BuildRequires:  ghc-test-framework-quickcheck2-devel
%endif
# End cabal-rpm deps

%description
This library is intended to be a comprehensive solution to parsing and
selecting quality-indexed values in HTTP headers. It is capable of parsing both
media types and language parameters from the Accept and Content header
families, and can be extended to match against other accept headers as well.
Selecting the appropriate header value is achieved by comparing a list of
server options against the quality-indexed values supplied by the client.

In the following example, the Accept header is parsed and then matched against
a list of server options to serve the appropriate media using 'mapAcceptMedia':

> getHeader >>= maybe send406Error sendResourceWith . mapAcceptMedia > [
("text/html", asHtml) > , ("application/json", asJson) > ]

Similarly, the Content-Type header can be used to produce a parser for request
bodies based on the given content type with 'mapContentMedia':

> getContentType >>= maybe send415Error readRequestBodyWith .
mapContentMedia > [ ("application/json", parseJson) > , ("text/plain",
parseText) > ]

The API is agnostic to your choice of server.


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
%doc CHANGES.md


%changelog
* Fri Sep 29 2017 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.7.1.1-1
- spec file generated by cabal-rpm-0.11.2
