from Model import db_connection
from Model import db_query
from fastapi.responses import JSONResponse

engine = db_connection.engineconn()
session = engine.sessionmaker()
commit = db_query.db_commit
close  = db_query.db_close

def pre_get_name():

    try:
        result = db_query.db_serch_name()

    except:
        result = JSONResponse(status_code=400, content="URL ERROR")

    else:
        if result == []:
            result = JSONResponse(status_code=404, content="Data Not Found")

    finally:
        session.close()

    return result