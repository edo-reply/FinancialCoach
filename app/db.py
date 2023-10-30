from dataclasses import fields, is_dataclass
from sqlite3 import connect

import config


class Repository:
    _connection = None

    def __init__(self, model_type: type):
        if Repository._connection is None:
            Repository._connection = connect(
                config.db_path, check_same_thread=False)
            with open(config.schema_path, "r") as schema_file:
                Repository._connection.executescript(schema_file.read())

        if not is_dataclass(model_type):
            raise ValueError(
                f"'{model_type.__name__}' is not a dataclass!")
        self.model_type: type = model_type
        self.table_name: str = model_type.__name__.lower()
        self.fields: list = [f.name for f in fields(model_type)]

    def select(self, **kwargs: str):
        query = f"SELECT {",".join(self.fields)} FROM {self.table_name} "\
            f"WHERE {",".join([f"{col} = ?" for col in kwargs.keys()])}"
        cursor = Repository._connection.execute(query, list(kwargs.values()))
        return cursor.fetchall()

    def insert(self, obj):
        if not isinstance(obj, self.model_type):
            raise ValueError(f"obj is of wrong type '{type(obj)}'")
        query = f"INSERT INTO {self.table_name} ({",".join(self.fields)}) "\
            f"VALUES ({",".join(["?"]*len(self.fields))})"
        values = [str(obj.__dict__[k]) for k in self.fields]
        Repository._connection.execute(query, values)

    def delete(self, **kwargs: str):
        query = f"DELETE FROM {self.table_name} "\
            f"WHERE {",".join([f"{col} = ?" for col in kwargs.keys()])}"
        Repository._connection.execute(query, list(kwargs.values()))
