

list_of_single_keywords = ["SELECT", "FROM", "WHERE", "GROUP BY", "HAVING", "UNION", "INTERSECT", "LIMIT", "INNER", "OUTER", "LEFT", "RIGHT", "ORDER", "GROUP"]
#special processing for order by, group by, inner/left/outer/right join


def SORT_keyword(sql_query, query_plan_dict):
    print("")

def LIMIT_keyword(sql_query, query_plan_dict):
    print("")

def AGGREGATE_keyword(sql_query, query_plan_dict):

    print("")

def SCAN_keyword(sql_query, query_plan_dict):
    print("")

def HASH_JOIN_keyword(sql_query, query_plan_dict):
    print("")

def UNIQUE_keyword(sql_query, query_plan_dict):
    print("")

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

    return print(new_sql_query)

def traverse_sql(sql_query, query_plan_keyword, query_plan_dict):
    sql_query = preprocess_sql(sql_query)

    if query_plan_keyword == "Sort":
        SORT_keyword(sql_query, query_plan_dict)

    elif query_plan_keyword == "Limit":
        LIMIT_keyword(sql_query, query_plan_dict)

    elif query_plan_keyword == "Aggregate":
        AGGREGATE_keyword(sql_query, query_plan_dict)

    elif query_plan_keyword == "Seq Scan" or query_plan_keyword == "Index Scan":
        SCAN_keyword(sql_query, query_plan_dict)

    elif query_plan_keyword == "Hash Join":
        HASH_JOIN_keyword(sql_query, query_plan_dict)

    elif query_plan_keyword == "Unique":
        UNIQUE_keyword(sql_query, query_plan_dict)

    else:
        print("Ignore")

    return print(sql_query)

