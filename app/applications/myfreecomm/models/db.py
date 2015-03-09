# -*- coding: utf-8 -*-
from gluon.tools import Auth
import os


#########################################################################
## #TODO isvaldo, documentar a configuração da base
#########################################################################


#  Variaveriaveis de ambiente, conf DB, /app/deploy/env_vars.sh

DATABASES = {
    'amazon': {
        'NAME': os.environ.get('RDS_DB_NAME'),
        'USER': os.environ.get('RDS_USERNAME'),
        'PASSWORD': os.environ.get('RDS_PASSWORD'),
        'HOST': os.environ.get('RDS_HOSTNAME'),
        'PORT': os.environ.get('RDS_PORT'),
    }
}


#################################
# @TODO isvaldo, documentar conexão
#
###########
db = DAL('mysql://%s:%s@%s:%s/%s'
         % (DATABASES['amazon']['USER'], DATABASES['amazon']['PASSWORD'],
           DATABASES['amazon']['HOST'], DATABASES['amazon']['PORT'],
           DATABASES['amazon']['NAME']))




## define auth
auth = Auth(db)

## create all tables needed by auth if not custom tables
auth.define_tables(username=False, signature=False)

## configure email
mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else 'smtp.gmail.com:587'
mail.settings.sender = 'you@gmail.com'
mail.settings.login = 'username:password'


## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

## if you need to use OpenID, Facebook, MySpace, Twitter, Linkedin, etc.
## register with janrain.com, write your domain:api_key in private/janrain.key
from gluon.contrib.login_methods.janrain_account import use_janrain
use_janrain(auth, filename='private/janrain.key')


##############################################
##########  BANCO DE DADOS  ##################
##############################################

## Tabela de itens.
db.define_table('item',
                Field('item_description'),
                Field('item_price'))

## Tabela de comerciante.
db.define_table('merchant',
                Field('merchant_name'),
                Field('merchant_address'))

## Tabela para registrar vendas.
db.define_table('sales',
                Field('purchaser_name'),
                Field('item_id', db.item),
                Field('merchant_id', db.merchant),
                Field('purchase_count'))

auth.enable_record_versioning(db)