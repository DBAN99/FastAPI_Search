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


# ----------------------- GET ---------------------------

def db_search_auto(name):
    result = session.query(company.company_name).filter(company.company_name.like('%{}%'.format(name))).first()

    return result

def db_serch_name(name):
    result = session.query(company.company_name).filter(company.company_name.like('%{}%'.format(name))).first()

    return result

def db_serch_tag(name):
    result = session.query(company.tag_name).filter(company.company_name.like('%{}%'.format(name))).first()

    return result

# -------------------------POST -----------------------------

def db_post_add(add):
    add_data = company(data=add)
    result = session.add(add_data)

    return result

def db_post_new():
    result = session.query(company.data).order_by(company.id.desc()).first()

    return result