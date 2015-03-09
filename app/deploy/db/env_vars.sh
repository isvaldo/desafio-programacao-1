#! /usr/bin/env bash

#for version control
export VERSION_CONTROL_TYPE=git
export BRANCH=$(CI_BRANCH)
export TAG=migrate-$(BRANCH)

#for database
export DB_TYPE=
export RDS_HOSTNAME=
export RDS_USERNAME=
export RDS_PASSWORD=
export RDS_DB_NAME=
export RDS_PORT=5432

#for web2py
export WEB2PY=$(TARGET_WEB2PY_DIR)
export APP=myfreedomm
