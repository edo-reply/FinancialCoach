from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Boolean, ForeignKey, MetaData, Table, Column, Integer, String, DateTime, func
from sqlalchemy.orm import registry

from models import User, Transaction


_registry = registry()

_metadata = MetaData()

_registry.map_imperatively(User,
    Table('users', _metadata,
        Column('id', String, primary_key=True),
        Column('first_name', String),
        Column('last_name', String),
        Column('budget', Integer)
    )
)

_registry.map_imperatively(Transaction,
    Table('user_transactions', _metadata,
        Column('id', String, primary_key=True),
        Column('user_id', String, ForeignKey('users.id')),
        Column('description', String),
        Column('amount', Integer),
        Column('category', Integer),
        Column('recurring_event', Boolean),
        Column('rating', Integer),
        Column('created_on', DateTime, default=func.now())
    )
)

db = SQLAlchemy(metadata=_metadata)
