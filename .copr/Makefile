# Getting the directory of the makefile actually being used is a real disaster for some reason
makedir := $(dir $(lastword $(MAKEFILE_LIST)))
topdir  := $(makedir)/..

RPM_NAME := $(notdir $(basename $(spec)))

srpm:
	dnf -y install git cabal-rpm
	# Figure out what we're building based on the spec argument
	case "$(notdir $(spec))" in \
		"bdcs.spec") CLONE_URL="https://github.com/weldr/bdcs.git" ; \
		             CABAL_PATH="bdcs.cabal" ; \
			     CABAL_SPEC_OPTIONS="-b" ;; \
	        "bdcs-api.spec") CLONE_URL="https://github.com/weldr/bdcs-api.git" ; \
		                 CABAL_PATH="bdcs-api.cabal" ; \
				 CABAL_SPEC_OPTIONS="-b" ;; \
		"bdcs-cli.spec") CLONE_URL="https://github.com/weldr/bdcs-cli.git" ; \
		                 CABAL_PATH="BDCSCli.cabal" ; \
				 CABAL_SPEC_OPTIONS="-b" ;; \
		"codec-rpm.spec") CLONE_URL="https://github.com/weldr/codec-rpm.git" ; \
		                  CABAL_PATH="codec-rpm.cabal" ;; \
		"content-store.spec") CLONE_URL="https://github.com/weldr/content-store.git" ; \
		                      CABAL_PATH="content-store.cabal" ;; \
                *) echo "Unknown spec file argument, add the project to .copr/Makefile" ; \
	           exit 1 ;; \
	esac ; \
	$(topdir)/makesrpm.sh "$(RPM_NAME)" "$$CLONE_URL" "$$CABAL_PATH" "$(outdir)" "$$CABAL_SPEC_OPTIONS"
