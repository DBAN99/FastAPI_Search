from sqlalchemy import Column, BigInteger,JSON
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Company(Base):
    __tablename__ = 'company'
    id = Column(BigInteger,nullable=False, autoincrement=True, primary_key=True)
    data = Column(JSON,nullable=True)
