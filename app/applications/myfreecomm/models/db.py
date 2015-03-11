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
##################################

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
mail.settings.server = 'logging' if request.is_local else 'smtp.mandrillapp.com'
mail.settings.sender = 'isvaldo.fernandes@gmail.com'
mail.settings.login = 'isvaldo.fernandes@gmail.com:sG-KmIL6VJ151dktJZ2fnw'


## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True


## Configurando Acesso via Oauth
from gluon.contrib.login_methods.janrain_account import use_janrain
use_janrain(auth, filename='private/janrain.key')


##############################################
##########  BANCO DE DADOS  ##################
##############################################

## Tabela de itens.
db.define_table('item',
                Field('description', 'text', notnull=True),
                Field('price', notnull=True, requires=IS_DECIMAL_IN_RANGE()))

## Tabela de comercio,
db.define_table('merchant',
                Field('name', notnull=True),
                Field('address', notnull=True))

## Tabela para registrar vendas.
db.define_table('sales',
                Field('purchaser_name',  notnull=True),
                Field('item_id', db.item, requires=IS_IN_DB(db, 'item.id', '%(description)s')),
                Field('merchant_id', db.merchant, requires=IS_IN_DB(db, 'merchant.id', '%(name)s')),
                Field('count',  notnull=True))

auth.enable_record_versioning(db)


#########################################
########## FILTROS PARA FK ##############
#########################################

## Filtros de Sales
db.sales.count.label = "Quantidade"
db.sales.purchaser_name.label = "Comprador"
db.sales.id.label = "Nº registro"


## Filtros de Merchant
db.merchant.name.label = "Nome"
db.merchant.address.label = "Endereço"
db.merchant.id.label = "Nº registro"


## Filtros de item
db.item.id.label = "Nº registro"
db.item.price.label = "Preço"
db.item.description.label = "Descrição"


###################################
#####Exportação em grid Config#####
###################################

