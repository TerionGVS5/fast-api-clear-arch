from sqlalchemy import Integer, String, Column

from app.database import Base


class Anime(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    year = Column(Integer)
