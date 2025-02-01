from sqlalchemy import create_engine
from sqlalchemy.orm import Session


PASSWORD = "peaceipreach"

POSTGRES_DATABASE_URL = f'postgresql+psycopg2://postgres:{PASSWORD}@localhost/ecommerce'


engine = create_engine(POSTGRES_DATABASE_URL)


session = Session(engine)