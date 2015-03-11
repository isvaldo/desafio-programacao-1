#! /usr/bin/env bash

#Configure conexão aqui caso não queria usar SQLITE
#export IS_AMAZON #variavel de controle de produção
export DB_TYPE=mysql 
export RDS_HOSTNAME=localhost
export RDS_USERNAME=root
export RDS_PASSWORD=myfreecomm123
export RDS_DB_NAME=myfreecomm
export RDS_PORT=3306

#for web2py
export WEB2PY=$(TARGET_WEB2PY_DIR)
export APP=myfreecomm
