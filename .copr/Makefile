# Getting the directory of the makefile actually being used is a real disaster for some reason
makedir := $(dir $(lastword $(MAKEFILE_LIST)))
topdir  := $(makedir)/..

RPM_NAME := $(notdir $(basename $(spec)))

srpm:
	dnf -y install git
	# Figure out what we're building based on the spec argument
	case "$(notdir $(spec))" in \
		"ghc-bdcs.spec") CLONE_URL="https://github.com/weldr/bdcs.git" ; \
		                 CABAL_PATH="src/bdcs.cabal" ;; \
                *) echo "Unknown spec file argument, add the project to .copr/Makefile" ; \
	           exit 1 ;; \
	esac ; \
	$(topdir)/makesrpm.sh "$(RPM_NAME)" "$$CLONE_URL" "$$CABAL_PATH" "$(outdir)"
