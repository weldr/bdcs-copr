Package of the dependencies of bdcs that are not already packages in Fedora

It's probably possible to automate these builds with the copr CLI, but on the
other hand that sounds like more work than it's worth. Here's the order to
build things in against F26:

* [ghc-memory-weldr](ghc-memory-weldr) (memory-0.14.7) ![ghc-memory-weldr status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-memory-weldr/status_image/last_build.png)
* [ghc-attoparsec-binary](ghc-attoparsec-binary) ![ghc-attoparsec-binary status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-attoparsec-binary/status_image/last_build.png)
* [ghc-chunked-data](ghc-chunked-data) ![ghc-chunked-data status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-chunked-data/status_image/last_build.png)
* [ghc-vector-algorithms](ghc-vector-algorithms) ![ghc-vector-algorithms status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-vector-algorithms/status_image/last_build.png)
* [ghc-mono-traversable](ghc-mono-traversable) ![ghc-mono-traversable status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-mono-traversable/status_image/last_build.png)
* [ghc-conduit-combinators](ghc-conduit-combinators) ![ghc-conduit-combinators status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-conduit-combinators/status_image/last_build.png)
* [ghc-codec-rpm](ghc-codec-rpm) ![ghc-codec-rpm status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-codec-rpm/status_image/last_build.png)
* [ghc-cond](ghc-cond) ![ghc-cond status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-cond/status_image/last_build.png)
* [ghc-cpu](ghc-cpu) ![ghc-cpu status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-cpu/status_image/last_build.png)
* [ghc-cryptonite-weldr](ghc-cryptonite-weldr) ![ghc-cryptonite-weldr status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-cryptonite-weldr/status_image/last_build.png)
* [ghc-persistent](ghc-persistent) ![ghc-persistent status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-persistent/status_image/last_build.png)
* [ghc-esqueleto](ghc-esqueleto) ![ghc-esqueleto status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-esqueleto/status_image/last_build.png)
* [ghc-haskell-gi-base](ghc-haskell-gi-base) ![ghc-haskell-gi-base status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-haskell-gi-base/status_image/last_build.png)
* [ghc-haskell-gi](ghc-haskell-gi) ![ghc-haskell-gi status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-haskell-gi/status_image/last_build.png)
* [ghc-haskell-gi-overloading](ghc-haskell-gi-overloading) ![ghc-haskell-gi-overloading status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-haskell-gi-overloading/status_image/last_build.png)
* [ghc-gi-glib](ghc-gi-glib) ![ghc-gi-glib status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-gi-glib/status_image/last_build.png)
* [ghc-gi-gobject](ghc-gi-gobject) ![ghc-gi-gobject status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-gi-gobject/status_image/last_build.png)
* [ghc-gi-gio](ghc-gi-gio) ![ghc-gi-gio status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-gi-gio/status_image/last_build.png)
* [ghc-gi-ostree](ghc-gi-ostree) ![ghc-gi-ostree status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-gi-ostree/status_image/last_build.png)
* [ghc-gitrev-weldr](ghc-gitrev-weldr) ![ghc-gitrev-weldr status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-gitrev-weldr/status_image/last_build.png)
* [ghc-asn1-types](ghc-asn1-types) ![ghc-asn1-types status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-asn1-types/status_image/last_build.png)
* [ghc-asn1-encoding](ghc-asn1-encoding) ![ghc-asn1-encoding status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-asn1-encoding/status_image/last_build.png)
* [ghc-asn1-parse](ghc-asn1-parse) ![ghc-asn1-parse status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-asn1-parse/status_image/last_build.png)
* [ghc-x509](ghc-x509) ![ghc-x509 status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-x509/status_image/last_build.png)
* [ghc-x509-store](ghc-x509-store) ![ghc-x509-store status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-x509-store/status_image/last_build.png)
* [ghc-x509-validation](ghc-x509-validation) ![ghc-x509-validation status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-x509-status/status_image/last_build.png)
* [ghc-x509-system](ghc-x509-system) ![ghc-x509-system status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-x509-system/status_image/last_build.png)
* [ghc-tls](ghc-tls) ![ghc-tls status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-tls/status_image/last_build.png)
* [ghc-connection](ghc-connection) ![ghc-connection status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-connection/status_image/last_build.png)
* [ghc-http-client-tls](ghc-http-client-tls) ![ghc-http-client-tls status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-http-client-tls/status_image/last_build.png)
* [ghc-http-conduit](ghc-http-conduit) ![ghc-http-conduit status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-http-conduit/status_image/last_build.png)
* [ghc-parsec-numbers](ghc-parsec-numbers) ![ghc-parsec-numbers status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-parsec-numbers/status_image/last_build.png)
* [ghc-persistent-sqlite](ghc-persistent-sqlite) ![ghc-persistent-sqlite status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-persistent-sqlite/status_image/last_build.png)
* [ghc-persistent-template](ghc-persistent-template) ![ghc-persistent-template status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-persistent-template/status_image/last_build.png)
* [ghc-hspec-expectations](ghc-hspec-expectations) ![ghc-hspec-expectations status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-hspec-expectations/status_image/last_build.png)
* [ghc-quickcheck-io](ghc-quickcheck-io) ![ghc-quickcheck-io status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-quickcheck-io/status_image/last_build.png)
* [ghc-hspec-core](ghc-hspec-core) ![ghc-hspec-core status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-hspec-core/status_image/last_build.png)
* [ghc-hspec-discover](ghc-hspec-discover) ![ghc-hspec-discover status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-hspec-discover/status_image/last_build.png)
* [ghc-hspec](ghc-hspec) ![ghc-hspec status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-hspec/status_image/last_build.png)
* [libgit2](libgit2) ![libgit2 status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/libgit2/status_image/last_build.png)
* [libgit2-glib](libgit2-glib) ![libgit2-glib status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/libgit2-glib/status_image/last_build.png)
* [ghc-gi-ggit](ghc-gi-ggit) ![ghc-gi-ggit status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-gi-ggit/status_image/last_build.png)
* [ghc-htoml](ghc-htoml) ![ghc-htoml status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-htoml/status_image/last_build.png)
* [ghc-distributive-weldr](ghc-distributive-weldr) ![ghc-distributive-weldr status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-distributive-weldr/status_image/last_build.png)
* [ghc-bifunctors](ghc-bifunctors) ![ghc-bifunctors status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-bifunctors/status_image/last_build.png)
* [ghc-semigroupoids](ghc-semigroupoids) ![ghc-semigroupoids status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-semigroupoids/status_image/last_build.png)
* [ghc-profunctors](ghc-profunctors) ![ghc-profunctors status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-profunctors/status_image/last_build.png)
* [ghc-free](ghc-free) ![ghc-free status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-free/status_image/last_build.png)
* [ghc-adjunctions](ghc-adjunctions) ![ghc-adjunctions status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-adjunctions/status_image/last_build.png)
* [ghc-kan-extensions](ghc-kan-extensions) ![ghc-kan-extensions status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-kan-extensions/status_image/last_build.png)
* [ghc-lens](ghc-lens) ![ghc-lens status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-lens/status_image/last_build.png)
* [ghc-lens-aeson](ghc-lens-aeson) ![ghc-lens-aeson status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-lens-aeson/status_image/last_build.png)
* [ghc-semver](ghc-semver) ![ghc-semver status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-semver/status_image/last_build.png)
* [ghc-crypto-pubkey-types](ghc-crypto-pubkey-types) ![ghc-crypto-pubkey-types](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-crypto-pubkey-types/status_image/last_build.png)
* [ghc-RSA](ghc-RSA) ![ghc-RSA](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-RSA/status_image/last_build.png)
* [ghc-authenticate-oauth](ghc-authenticate-oauth) ![ghc-authenticate-oauth status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-authenticate-oauth/status_image/last_build.png)
* [ghc-psqueues-weldr](ghc-psqueues-weldr) ![ghc-psqueues-weldr status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-psqueues-weldr/status_image/last_build.png)
* [ghc-wreq](ghc-wreq) ![ghc-wreq status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-wreq/status_image/last_build.png)

Fedora 27 already has a sufficiently new version of libgit2.
Fedora 27 does *not* have the following, due to the ongoing Beta freeze:
  * [ghc-hourglass](ghc-hourglass). Build before ghc-asn1-types.
  * [ghc-http-api-data](ghc-http-api-data). Build before ghc-persistent.
  * [ghc-microlens-th](ghc-microlens-th). Build before ghc-persistent-sqlite.
  * [ghc-aeson-compat](ghc-aeson-compat). Build before ghc-persistent-template.
  * [ghc-pem](ghc-pem). Build before ghc-x509.
  * [ghc-http-client](ghc-http-client). Build before ghc-authenticate-oauth.
  * [ghc-socks](ghc-socks). Build before ghc-connection.
  * [ghc-comonad](ghc-comonad). Build before ghc-bifunctors.

Rawhide has the following packages:
  * ghc-bifunctors
  * ghc-esqueleto
  * ghc-persistent
  * ghc-persistent-sqlite
  * ghc-persistent-template
  * new enough libgit2

Rawhide has a sufficiently new version of ghc-cryptonite, but build -weldr
anyway to relink against ghc-memory-weldr.
