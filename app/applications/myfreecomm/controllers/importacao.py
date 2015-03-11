# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - api is an example of Hypermedia API support and access control
#########################################################################
from import_filter import SalesImport
from pyheaderfile import Csv
import os


def index():
    ## Configuração do formulario para upload
    form = SQLFORM.factory(
        Field('arquivo', 'upload',
              uploadfolder=os.path.join(request.folder, 'uploads'),
              requires=IS_UPLOAD_FILENAME(extension='tab')),
        submit_button="importar")

    ## Tratativa condicionada a aceitação do formulario
    if form.process().accepted:
        file_csv = Csv(name=os.path.join(request.folder, 'uploads', form.vars.arquivo),
                       encode="utf-8",
                       strip=True,
                       delimiters=["\t"])
        ## Configurando db
        sales_import = SalesImport(db=db)

        try:
            ## formatando dados do arquivo para banco
            for row in file_csv.read():
                sales_import(row=row).format()
        except:
            response.flash = "Erro ao processar arquivo, verifique a formatação"
            return dict(form=form)

        sales_import.insert_all()

        response.flash = "Arquivo importado com sucesso"

    return dict(form=form)


def get_receita():
    """
    Retorna receita separada por itens e total
    :return:
    """
    receita = dict()
    receita['query'] = db((db.sales.item_id == db.item.id) &
                          (db.sales.merchant_id == db.merchant.id)).select(db.item.price, db.sales.count)

    ## Multiplica preço pela quantidade usando list of comprehension, soma o resultado
    receita['valor_total'] = sum(
        [float(tabela.item.price) * float(tabela.sales.count) for tabela in receita['query']]
    )


    return dict(receita=receita)