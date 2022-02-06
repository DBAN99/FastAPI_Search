from sqlalchemy import Column, BigInteger, JSON, Computed,VARCHAR
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Company(Base):
    __tablename__ = 'company'
    id = Column(BigInteger,nullable=False, autoincrement=True, primary_key=True)
    data = Column(JSON,nullable=True)

    company_name = Column(JSON, Computed("JSON_EXTRACT(data, '$.company')"))
    tag_name = Column(JSON, Computed("JSON_EXTRACT(data, '$.tag_name')"))

    company_name_en = Column(VARCHAR(255), Computed("JSON_EXTRACT(company_name, '$.en')"))
    company_name_ko = Column(VARCHAR(255), Computed("JSON_EXTRACT(company_name, '$.ko')"))
    company_name_ja = Column(VARCHAR(255), Computed("JSON_EXTRACT(company_name, '$.ja')"))

    tag_name_en = Column(VARCHAR(255), Computed("JSON_EXTRACT(tag_name, '$.en')"))
    tag_name_ko = Column(VARCHAR(255), Computed("JSON_EXTRACT(tag_name, '$.ko')"))
    tag_name_ja = Column(VARCHAR(255), Computed("JSON_EXTRACT(tag_name, '$.ja')"))


# alter table company add company_name JSON as (JSON_EXTRACT(data, '$.company')) stored, add fulltext (company_name);
# alter table company add tag_name JSON as (JSON_EXTRACT(data, '$.tag_name')) stored, add fulltext (tag_name);

# alter table company add company_name_en VARCHAR(255) as (JSON_EXTRACT(company_name, '$.en')) stored, add fulltext (company_name_en);
# alter table company add company_name_ko VARCHAR(255) as (JSON_EXTRACT(company_name, '$.ko')) stored, add fulltext (company_name_ko);
# alter table company add company_name_ja VARCHAR(255) as (JSON_EXTRACT(company_name, '$.ja')) stored, add fulltext (company_name_ja);

# alter table company add tag_name_en VARCHAR(255) as (JSON_EXTRACT(tag_name, '$.en')) stored, add fulltext (tag_name_en);
# alter table company add tag_name_ko VARCHAR(255) as (JSON_EXTRACT(tag_name, '$.ko')) stored, add fulltext (tag_name_ko);
# alter table company add tag_name_ja VARCHAR(255) as (JSON_EXTRACT(tag_name, '$.ja')) stored, add fulltext (tag_name_ja);

# ALTER TABLE company ADD FULLTEXT (company_name, tag_name);
# ALTER TABLE company ADD FULLTEXT INDEX idx_company_name (company_name_en,company_name_ko,company_name_ja) VISIBLE;

