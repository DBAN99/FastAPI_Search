from fastapi import HTTPException

from Model import db_connection
from Model import db_query
from fastapi.responses import JSONResponse

engine = db_connection.engineconn()
session = engine.sessionmaker()
commit = db_query.db_commit
close  = db_query.db_close

def pre_get_auto_name(name,language):

    try:
        result = db_query.db_search_auto(name)

    except:
        raise HTTPException(status_code=400, detail="URL ERROR")
        # result = JSONResponse(status_code=400, content="URL ERROR")

    else:
        if result == []:
            # result = JSONResponse(status_code=404, content="Data Not Found")
            raise HTTPException(status_code=404, detail="Data Not Found")

        #검색시 2개 이상의 데이터가 왔을 때는 어떻게 처리?
        result = result["company_name"][language]

        if result == "null":
            raise HTTPException(status_code=404, detail="Data Not Found")

    finally:
        session.close()

    return result

def pre_get_language_name(name, language):

    try:
        search_company = db_query.db_serch_name(name)
        search_tag = db_query.db_serch_tag(name)

    except:
        raise HTTPException(status_code=400, detail="URL ERROR")
        # result = JSONResponse(status_code=400, content="URL ERROR")

    else:
        result = {}

        if search_company == None:
            # result = JSONResponse(status_code=404, content="Data Not Found")
            raise HTTPException(status_code=404, detail="Data Not Found")

        result["company_name"] = search_company["company_name"][language]
        result["tag_name"] = search_tag["tag_name"][language]

    finally:
        session.close()

    return result
