# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - api is an example of Hypermedia API support and access control
#########################################################################


@auth.requires_login()
def index():
    """
    Pagina inicial
    @TODO isvaldo, bolar algo legal aqui
    """
    response.flash = T("Bem vindo, Sales import")

    return dict()


@auth.requires_login()
def editar():
    """
    Recebe como parametro Args, retorna um grid da tabela
    correspondende, retorna em 404 para valores invalidos
    """

    ## Filtro para representar tabelas na grid
    if not request.args(0):
        db.sales.item_id.label = "Preço item"
        db.sales.merchant_id.label = "Mercador"
        db.sales.item_id.filter_out = lambda id: 'R$ '+db(db.item.id == id).select(db.item.price).first().price
        db.sales.merchant_id.filter_out = lambda id: db(db.merchant.id == id).select(db.merchant.name).first().name


    ## recebe parametro table e mostra a grid correspondente
    targe_table = request.vars.table
    if targe_table in ['sales', 'item', 'merchant']:
        grid = SQLFORM.grid(db[targe_table], advanced_search=False)
    else:
        raise HTTP(404, "Pagina não encontrada")

    return dict(grid=grid)


def user():
    """
    Pagina para controle de acesso, login,registro,recuperação de senha
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_login() 
def api():
    """
    this is example of API with access control
    WEB2PY provides Hypermedia API (Collection+JSON) Experimental
    """
    from gluon.contrib.hypermedia import Collection
    rules = {
        '<tablename>': {'GET': {}, 'POST': {}, 'PUT': {}, 'DELETE': {}},
        }
    return Collection(db).process(request, response, rules)
