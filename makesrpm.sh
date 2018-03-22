#!/bin/sh

if [ "$#" -lt 2 ]; then
    echo "Usage: makesrpm.sh <rpm-name> <clone-url> <.cabal-path> <output directory> [<cabal-spec options>]"
    echo "Example: makesrpm.sh ghc-bdcs https://github.com/weldr/bdcs.git src/bdcs.cabal \$outdir"
    exit 1
fi

rpm_name="$1"
clone_url="$2"
cabal_path="$3"
outdir="$4"
options="$5"

tmpdir="$(mktemp -d makesrpm.XXXXXX)"
trap 'rm -rf "$tmpdir"' EXIT

# Clone the source
( cd "$tmpdir" &&
  git clone "$clone_url" srcdir &&

  # Create the spec file
  ( cd srcdir/"$(dirname "$cabal_path")" &&

    pkgname="$(basename "$cabal_path" .cabal)" &&

    # Fix the name if it isn't what cabal-rpm thinks it should be
    cabal_rpm_name="$(cabal-rpm spec $options "$pkgname")" &&
    if [ "$cabal_rpm_name" != "$rpm_name" ]; then
        mv "${cabal_rpm_name}.spec" "${rpm_name}.spec"
        sed -i "s/^Name:.*/Name: ${rpm_name}/" "${rpm_name}.spec"
    fi &&

    # Replace the release with the date
    # Can only make one release per day
    sed -i "s/^Release:.*/Release: 0.$(date +%Y%m%d)git$(git rev-parse --short HEAD)/" "$rpm_name".spec &&

    # Replace the URL with the github link
    sed -i "s|^Url:.*|Url: $clone_url|" "$rpm_name".spec &&

    # Replace the Source0 line with something easier
    sed -i "s/^Source0:.*/Source0: %{pkg_name}.tar.gz/" "$rpm_name".spec &&

    # cabal-rpm doesn't know about the bdcs files installed to libexec, since that's
    # handled by Setup.hs and not something directly in the .cabal file. Delete the
    # libexec executables and just include a line for /usr/libexec/weldr/
    if [ "$rpm_name" = "bdcs" ]; then
        sed -i '/^%{_bindir}\/bdcs-/d' "$rpm_name".spec &&
        sed -i '/^%{_bindir}\/inspect-/d' "$rpm_name".spec
        sed -i '/^%files$/a\
%{_libexecdir}/weldr/' "$rpm_name".spec
    fi &&

    pkgver="$(rpm -q --specfile "${rpm_name}.spec" --qf '%{VERSION}\n' | head -1)" &&

    # Create the source archive
    git archive -o "$(basename "$cabal_path" .cabal).tar.gz" --prefix="$rpm_name-$pkgver/" HEAD &&

    # Create the srpm
    rpmbuild -bs -D '_sourcedir .' -D '_srcrpmdir .' "${rpm_name}".spec
  )
)

if [ $? -ne 0 ]; then
    echo "Error creating SRPM"
    exit 1
fi

[ -d "$outdir" ] || mkdir -p "$outdir"
mv "$tmpdir/srcdir/$(dirname "$cabal_path")/${rpm_name}"*.src.rpm "$outdir"
