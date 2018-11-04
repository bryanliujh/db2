

list_of_single_keywords = ["SELECT", "FROM", "WHERE", "GROUP BY", "HAVING", "UNION", "INTERSECT", "LIMIT", "INNER", "OUTER", "LEFT", "RIGHT", "ORDER", "GROUP"]
#special processing for order by, group by, inner/left/outer/right join


def LIMIT_keyword(query_plan_dict_item):
    sql_match = "LIMIT " + str(query_plan_dict_item["Actual Rows"])
    query_plan_dict_item["Sql"] = sql_match

def AGGREGATE_keyword(query_plan_dict_item):
    sql_match = ""
    for i in query_plan_dict_item["Group Key"]:
        sql_match = sql_match + i
    sql_match = "GROUP BY " + sql_match
    query_plan_dict_item["Sql"] = sql_match

def SCAN_keyword(query_plan_dict_item):
    alias = ""
    if query_plan_dict_item["Relation Name"] == query_plan_dict_item["Alias"]:
        alias = ""
    else:
        alias = query_plan_dict_item["Alias"]
    sql_match = query_plan_dict_item["Relation Name"] + " " + alias
    query_plan_dict_item["Sql"] = sql_match

def HASH_JOIN_keyword(query_plan_dict_item):
    sql_match = str(query_plan_dict_item["Join Type"]) + " JOIN ON " + str(query_plan_dict_item["Hash Cond"])
    query_plan_dict_item["Sql"] = sql_match

def UNIQUE_keyword(query_plan_dict_item):
    sql_match = ""
    for i in query_plan_dict_item["Output"]:
        sql_match = sql_match + i
    sql_match = "DISTINCT " + sql_match
    query_plan_dict_item["Sql"] = sql_match


def preprocess_sql(sql_query):
    #convert to upper case
    sql_query = sql_query.upper()
    new_sql_query = ""
    for word in sql_query.split():
        # strip carriage return and newline
        word = word.rstrip('\r\n')
        if word in list_of_single_keywords:
                word = "\n" + word

        new_sql_query = new_sql_query + " " + word

    return new_sql_query

def traverse_sql(sql_query, query_plan_dict_item):
    sql_query = preprocess_sql(sql_query)
    query_plan_keyword = query_plan_dict_item["Node Type"]

    if query_plan_keyword == "Limit":
        LIMIT_keyword(query_plan_dict_item)

    elif query_plan_keyword == "Aggregate":
        AGGREGATE_keyword(query_plan_dict_item)

    elif query_plan_keyword == "Seq Scan" or query_plan_keyword == "Index Scan" or query_plan_keyword == "Index Only Scan":
        SCAN_keyword(query_plan_dict_item)

    elif query_plan_keyword == "Hash Join":
        HASH_JOIN_keyword(query_plan_dict_item)

    elif query_plan_keyword == "Unique":
        UNIQUE_keyword(query_plan_dict_item)


    else:
        query_plan_dict_item["Sql"] = ""

    return print(sql_query)

