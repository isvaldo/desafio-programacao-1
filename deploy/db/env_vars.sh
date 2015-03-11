#! /usr/bin/env bash

#for version control
export VERSION_CONTROL_TYPE=git
export BRANCH=$(CI_BRANCH)
export TAG=migrate-$(BRANCH)

#for database,for security, configure the variables in the production environment manually
export DB_TYPE=mysql
export RDS_HOSTNAME=localhost
export RDS_USERNAME=root
export RDS_PASSWORD=myfreecomm123
export RDS_DB_NAME=myfreecomm
export RDS_PORT=3306

#for web2py
export WEB2PY=$(TARGET_WEB2PY_DIR)
export APP=myfreecomm
