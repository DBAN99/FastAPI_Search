from sqlalchemy import text
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



# Company
def db_serch_name():
    result = session.query(company.data).filter(company.data.comparator['tags']=="원티드랩").all()

    return result