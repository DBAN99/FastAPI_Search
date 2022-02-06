from Model import db_connection
from Model import db_class

engine = db_connection.engineconn()
session = engine.sessionmaker()

company = db_class.Company


# COMMIT
def db_commit():
    return session.commit()

# CLOSE
def db_close():
    return session.close()

def db_search_auto():
    result = session.query(company.company_name).filter(company.company_name.like('%원티%')).all()

    return result

# --------------------------------------------------

def db_serch_name(name):
    result = session.query(company.company_name,company.tag_name).filter(company.company_name.match(name)).first()

    return result
