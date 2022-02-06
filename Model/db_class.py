from sqlalchemy import Column, BigInteger, JSON, Computed
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Company(Base):
    __tablename__ = 'company'
    id = Column(BigInteger,nullable=False, autoincrement=True, primary_key=True)
    data = Column(JSON,nullable=True)

    company_name = Column(JSON, Computed("JSON_EXTRACT(data, '$.company')"))
    tag_name = Column(JSON, Computed("JSON_EXTRACT(data, '$.tag_name')"))
