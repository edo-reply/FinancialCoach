from dataclasses import fields, is_dataclass
from sqlite3 import connect

import config


class Repository:
    _connection = None

    def __init__(self, model_type: type):
        if not is_dataclass(model_type):
            raise ValueError(
                f"'{model_type.__name__}' is not a dataclass!")
        self.model_type: type = model_type
        self.table_name: str = model_type.__name__.lower()
        self.fields: list = [f.name for f in fields(model_type)]

    @classmethod
    def init_db(cls):
        if cls._connection is None:
            cls._connection = connect(
                config.db_path, check_same_thread=False)
            with open(config.schema_path, "r") as schema_file:
                cls._connection.executescript(schema_file.read())

    def select(self, **kwargs: str) -> list:
        query = f"SELECT {",".join(self.fields)} FROM {self.table_name} "\
            f"WHERE {",".join([f"{col} = ?" for col in kwargs.keys()])}"
        cursor = Repository._connection.execute(query, list(kwargs.values()))
        result = [self.model_type(**dict(zip(self.fields, result)))
                  for result in cursor.fetchall()]
        return result

    def insert(self, obj) -> bool:
        if not isinstance(obj, self.model_type):
            raise ValueError(f"obj is of wrong type '{type(obj)}'")
        query = f"INSERT INTO {self.table_name} ({",".join(self.fields)}) "\
            f"VALUES ({",".join(["?"]*len(self.fields))})"
        values = [str(obj.__dict__[k]) for k in self.fields]
        cursor = Repository._connection.execute(query, values)
        return cursor.rowcount == 1

    def delete(self, **kwargs: str) -> int:
        query = f"DELETE FROM {self.table_name} "\
            f"WHERE {",".join([f"{col} = ?" for col in kwargs.keys()])}"
        cursor = Repository._connection.execute(query, list(kwargs.values()))
        return cursor.rowcount
