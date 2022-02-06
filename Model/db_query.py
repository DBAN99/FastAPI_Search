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

def db_search_auto(name):
    result = session.query(company.company_name).filter(company.company_name.like('%{}%'.format(name))).all()

    return result

# --------------------------------------------------

def db_serch_name(name):
    result = session.query(company.company_name).filter(company.company_name.like('%{}%'.format(name))).first()

    return result

def db_serch_tag(name):
    result = session.query(company.tag_name).filter(company.company_name.like('%{}%'.format(name))).first()

    return result
