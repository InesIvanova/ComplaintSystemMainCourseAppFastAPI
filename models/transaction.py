import sqlalchemy
from db import metadata


transaction = sqlalchemy.Table(
    "transactions",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("quote_id", sqlalchemy.String(120), nullable=False),
    sqlalchemy.Column("transfer_id", sqlalchemy.Integer, nullable=False),
    sqlalchemy.Column("target_account_id", sqlalchemy.String(100), nullable=False),
    sqlalchemy.Column("amount", sqlalchemy.Float, nullable=False),
    sqlalchemy.Column("amount", sqlalchemy.Float, nullable=False),
    sqlalchemy.Column("complaint_id", sqlalchemy.ForeignKey("complaints.id"))
)