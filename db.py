import databases
import sqlalchemy
from decouple import config

DATABASE_URL = f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}@localhost:5433/complaints"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
