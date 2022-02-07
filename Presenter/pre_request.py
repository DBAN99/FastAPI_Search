from fastapi import HTTPException

from Model import db_connection
from Model import db_query
from fastapi.responses import JSONResponse

engine = db_connection.engineconn()
session = engine.sessionmaker()
commit = db_query.db_commit
close = db_query.db_close

# ---------------------- GET ------------------------------

def pre_get_auto_name(name,language):

    try:
        result = db_query.db_search_auto(name)
        result = {"company_name": result["company_name"][language]}

    except:
        raise HTTPException(status_code=400, detail="URL ERROR")

    else:
        if result == []:
            raise HTTPException(status_code=404, detail="Data Not Found")

        elif result == "null":
            raise HTTPException(status_code=404, detail="Data Not Found")

    finally:
        session.close()

    return result

def pre_get_language_name(name, language):

    try:
        result = {}
        search_company = db_query.db_serch_name(name)
        search_tag = db_query.db_serch_tag(name)

        result["company_name"] = search_company["company_name"][language]
        result["tags"] = search_tag["tag_name"][language]

    except:
        raise HTTPException(status_code=400, detail="URL ERROR")

    else:
        if search_company == None:
            raise HTTPException(status_code=404, detail="Data Not Found")


    finally:
        session.close()

    return result

# -------------------- POST -------------------------
def pre_post_add(add,language):

    try:
        name_data = add.company_name
        tag_data = add.tags

        query_data = json_control(tag_data, name_data)
        db_query.db_post_add(query_data)
        db_query.db_commit()
        db_data = db_query.db_post_new()
        result = {}

        result["company_name"] = db_data["data"]["company"][language]
        result["tags"] = db_data["data"]["tag_name"][language]

    except:
        result = JSONResponse(status_code=400, content="URL ERROR")

    else:
        pass

    finally:
        session.close()

    return result


# ----------- 데이터 형식을 맞추기 위한 처리----------------
def json_control(data_tag,data_name):

    list_len = len(data_tag)
    tag_data = data_tag[0]["tag_name"]

    keys = tag_data.keys()

    list_key = list(keys)
    key_len = len(list_key)

    language_tag = {}

    for i in range(list_len):
        tags = ""
        for j in range(key_len):

            tags_data = data_tag[i]["tag_name"][list_key[j]]

            if j == 0:
                tags += tags_data
            else:
                tags += "|" + tags_data

        language_tag[list_key[i]] = tags

    result_data = {}
    result_data["company"] = data_name
    result_data["tag_name"] = language_tag

    return result_data