# ----------------------------------------------------------------------------
# Makefile for make4py-example
#
# Copyright (c) 2023 by Clemens Rabe <clemens.rabe@clemensrabe.de>
# All rights reserved.
# This file is part of syncer (https://github.com/seeraven/make4py-example)
# and is released under the "BSD 3-Clause License". Please see the LICENSE file
# that is included as part of this package.
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
#  SETTINGS
# ----------------------------------------------------------------------------
APP_NAME             := make4py-example
APP_VERSION          := 0.0.1
UBUNTU_DIST_VERSIONS := 18.04 20.04 22.04

# To use our own pylintrc file, we simply set the variables befor including make4py:
PYLINT_RCFILE        := $(CURDIR)/.pylintrc


# ----------------------------------------------------------------------------
#  MAKE4PY INTEGRATION
# ----------------------------------------------------------------------------
include .make4py/make4py.mk


# ----------------------------------------------------------------------------
#  EOF
# ----------------------------------------------------------------------------
