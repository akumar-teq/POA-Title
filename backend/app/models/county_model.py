from sqlalchemy import Column, Integer, String
from app.core.database import Base

class County(Base):
    __tablename__ = "counties"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    website = Column(String, nullable=True)
