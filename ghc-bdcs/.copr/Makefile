# Set these two per-package
CLONE_URL  := https://github.com/weldr/bdcs.git
CABAL_PATH := src/bdcs.cabal

# Getting the directory of the makefile actually being used is a real disaster for some reason
makedir := $(dir $(lastword $(MAKEFILE_LIST)))
topdir  := $(makedir)/../..

RPM_NAME := $(notdir $(basename $(spec)))

srpm:
	$(topdir)/makesrpm.sh $(RPM_NAME) $(CLONE_URL) $(CABAL_PATH) $(outdir)
