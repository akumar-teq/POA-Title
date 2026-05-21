from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Request(Base):
    __tablename__ = "requests"

    id = Column(Integer, primary_key=True, index=True)
    homeowner_name = Column(String)
    county = Column(String)
    status = Column(String, default="pending")
