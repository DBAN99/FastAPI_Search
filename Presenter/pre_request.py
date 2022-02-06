from Model import db_connection
from Model import db_query
from fastapi.responses import JSONResponse

engine = db_connection.engineconn()
session = engine.sessionmaker()
commit = db_query.db_commit
close  = db_query.db_close

def pre_get_auto_name(name,language):

    try:
        result = name
    except:
        result = JSONResponse(status_code=400, content="URL ERROR")

    else:
        if result == []:
            result = JSONResponse(status_code=404, content="Data Not Found")

    finally:
        session.close()

    return result

def pre_get_language_name(name, language):

    try:
        result = db_query.db_serch_name(name)
        print(language)

    except:
        result = JSONResponse(status_code=400, content="URL ERROR")

    else:
        if result == [] or result == 'null':
            result = JSONResponse(status_code=404, content="Data Not Found")

    finally:
        session.close()

    return result

def pre_get_fulltext_name():

    try:
        result = db_query.db_fulltext()

    except:
        result = JSONResponse(status_code=400, content="URL ERROR")

    else:
        if result == []:
            result = JSONResponse(status_code=404, content="Data Not Found")

    finally:
        session.close()

    return result