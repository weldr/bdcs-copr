#!/bin/sh

if [ "$#" -lt 2 ]; then
    echo "Usage: makesrpm.sh <rpm-name> <clone-url> <.cabal-path> <output directory>"
    echo "Example: makesrpm.sh ghc-bdcs https://github.com/weldr/bdcs.git src/bdcs.cabal \$outdir"
    exit 1
fi

rpm_name="$1"
clone_url="$2"
cabal_path="$3"
outdir="$4"

tmpdir="$(mktemp -d makesrpm.XXXXXX)"
trap 'rm -rf "$tmpdir"' EXIT

# Clone the source
( cd "$tmpdir" &&
  git clone "$clone_url" srcdir &&

  # Create the spec file
  ( cd srcdir/"$(dirname "$cabal_path")" &&
    cabal-rpm spec "$(basename "$cabal_path" .cabal)" &&

    # Replace the release with the date
    # Can only make one release per day
    sed -i "s/^Release:.*/Release: 0.$(date +%Y%m%d)git$(git rev-parse --short HEAD)/" "$rpm_name".spec &&

    # Replace the URL with the github link
    sed -i "s|^Url:.*|Url: $clone_url|" "$rpm_name".spec &&

    # Replace the Source0 line with something easier
    sed -i "s/^Source0:.*/Source0: %{pkg_name}.tar.gz/" "$rpm_name".spec &&

    # Create the source archive
    git archive -o "$(basename "$cabal_path" .cabal).tar.gz" HEAD &&

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
