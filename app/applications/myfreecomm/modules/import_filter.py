# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

from pyheaderfile import Csv

class SqlImport:
    """
    Class modelo para importação, essa classe vai carregar o comportamento em comum
    entre outras classes de importação.

    """
    def __init__(self, **kwargs):
        self.db = kwargs['db']
        self.to_insert = []

    def __insert(self, row):
        pass

    def __update(self, row):
        pass

    def __delete(self, row):
        pass


class SalesImport(SqlImport):
    """
    Class para importar Sales
    """

    def __init__(self, **kwargs):

        SqlImport.__init__(self, **kwargs)

        # Mapeamento, mapeia as entradas com entidades do db
        self.map_tables = dict(description="item description",
                               price="item price",
                               name="merchant name",
                               address="merchant address",
                               purchaser_name="purchaser name",
                               count="purchase count")

    def __call__(self, **kwargs):
        """
        Para cada chamada uma nova linha é pré-configurada
        :param row: dict
        :return: self
        """
        self.row = kwargs['row']
        self.row_map = dict()
        return self

    def __sort_dict(self):
        """
        Mapeia os campos conforme definido em map_tables
        :return:
        """
        for table in self.map_tables.keys():
            self.row_map[table] = self.row[str(self.map_tables[table]).decode(encoding="utf-8")]

    def __insert(self, row):
        """
        Registra itens, merchant, sales
        :return:
        """
        row['item_id'] = self.db.item.insert(**self.db.item._filter_fields(row))
        row['merchant_id'] = self.db.merchant.insert(**self.db.merchant._filter_fields(row))
        self.db.sales.insert(**self.db.sales._filter_fields(row))

    def format(self):
        """
        Aponta as colunas do arquivo para tabelas do db, adiciona o resultado em to_insert
        :return:
        """
        self.__sort_dict()
        self.to_insert.append(self.row_map)

    def insert_all(self):
        """
        Da insert em todos os dados em to_insert
        :return:
        """
        for row in self.to_insert:
            self.__insert(row)


















