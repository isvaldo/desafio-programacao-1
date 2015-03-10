# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations


class SqlImport:
    """
    Class para importar @TODO, isvaldo DOCUMENTAR CLASS AQUI

    """
    def __init__(self, db):
        self.db = db

    def insert(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


class SalesImport(SqlImport):
    """
    Class para importação/analise de vendas
    """

    def __init__(self, db):

        SqlImport.__init__(self, db)

        self.row_map = dict()
        # Mapeamento, mapeia as entradas com entidades do db
        self.map_tables = dict(description="item description",
                               price="item price",
                               name="merchant name",
                               address="merchant address",
                               purchaser_name="purchaser name",
                               count="purchase count")

    def __call__(self, row):
        """
        Para cada chamada uma nova linha é pré-configurada
        :param row: dict
        :return: self
        """
        self.row = row
        self.sort_dict()
        return self

    def sort_dict(self):
        """
        Mapeia os campos conforme definido em map_tables
        :return:
        """
        for table in self.map_tables.keys():
            self.row_map[table] = self.row[str(self.map_tables[table]).decode(encoding="utf-8")]

    def insert(self):
        """
        Verifica duplicidades, Faz Insert no banco de dados
        :return:
        """
        print self.row_map['price']










