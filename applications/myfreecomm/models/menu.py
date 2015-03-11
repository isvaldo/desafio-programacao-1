# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Configuração do menu
#########################################################################

response.logo = A('Sales Import',
                  _class="brand", _href="")
response.title = "Sales Import"
response.subtitle = ''

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Isvaldo Fernandes <isvaldo.fernandes@gmail.com>'
response.meta.keywords = 'Finance,sales,price'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## Configurando Menu e sub menu
#########################################################################
if auth.is_logged_in():
    response.menu = [
        (T('Home'), False, URL('default', 'index'), []),
        (T('Edição'), False, '', [
            (T('Editar Produtos'), False, URL('default', 'editar', vars=dict(table='item')), []),
            (T('Editar Comércio'), False, URL('default', 'editar', vars=dict(table='merchant')), []),
            (T('Editar Vendas'), False, URL('default', 'editar', vars=dict(table='sales')), [])
        ]),
        (T('Importação'), False, URL('importacao', 'index'), [])
]

DEVELOPMENT_MENU = True

#########################################################################
## provide shortcuts for development. remove in production
#########################################################################

def _():
    # shortcuts
    app = request.application
    ctr = request.controller
    # useful links to internal and external resources
    response.menu += []


if DEVELOPMENT_MENU: _()

if "auth" in locals(): auth.wikimenu() 
