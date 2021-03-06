from typing import Type

from tortoise import Model
from tortoise.backends.sqlite.schema_generator import SqliteSchemaGenerator
from tortoise.fields import Field

from aerich.ddl import BaseDDL
from aerich.exceptions import NotSupportError


class SqliteDDL(BaseDDL):
    schema_generator_cls = SqliteSchemaGenerator
    DIALECT = SqliteSchemaGenerator.DIALECT

    def drop_column(self, model: "Type[Model]", column_name: str):
        raise NotSupportError("Drop column is not support in SQLite.")

    def modify_column(self, model: "Type[Model]", field_object: Field):
        raise NotSupportError("Modify column is not support in SQLite.")
    def rename_column(self, model: "Type[Model]", old_column_name, field_object: Field):
        raise NotSupportError("Rename column is not support in SQLite.")

