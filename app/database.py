from uuid import uuid4
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Boolean, ForeignKey, Transaction, MetaData, Table, Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import registry

from models.user import User
from models.transaction import Transaction

sqlregistry = registry()

metadata = MetaData()

sqlregistry.map_imperatively(User,
    Table('users', metadata,
        Column('id', String, primary_key=True, default=lambda: str(uuid4())),
        Column('first_name', String),
        Column('last_name', String),
        Column('budget', Integer)
    )
)

sqlregistry.map_imperatively(Transaction,
    Table('user_transactions', metadata,
        Column('id', String, primary_key=True, default=lambda: str(uuid4())),
        Column('user_id', String, ForeignKey("users.id")),
        Column('description', String),
        Column('amount', Integer),
        Column('category', Integer),
        Column('recurring_event', Boolean),
        Column('rating', Integer),
        Column('created_on', TIMESTAMP)
    )
)

db = SQLAlchemy(metadata=metadata)
