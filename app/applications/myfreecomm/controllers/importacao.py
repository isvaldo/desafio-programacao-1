# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - api is an example of Hypermedia API support and access control
#########################################################################

from pyheaderfile import Csv
import os


def index():
    form = SQLFORM.factory(
        Field('arquivo', 'upload', uploadfolder=os.path.join(request.folder, 'uploads')),
        submit_button="importar")

    if form.process().accepted:
        file_csv = Csv(name=os.path.join(request.folder, 'uploads', form.vars.arquivo),
                       encode="utf-8",
                       strip=True,
                       delimiters=["\t"])

        for row in file_csv.read():


        response.flash = "Arquivo importado com sucesso"



    return dict(form=form)