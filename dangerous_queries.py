#!/usr/bin/python3

dangerous_postgresql_queries = {
    "dangerous_query1": "SELECT version()",
    "dangerous_query2": "SELECT * FROM information_schema.tables",
    "dangerous_query3": "'foo'||'bar'"
}

dangerous_mysql_queries = {
    "dangerous_query1": "SELECT @@version",
    "dangerous_query2": "SELECT * FROM information_schema.tables",
    "dangerous_query3": "'foo' 'bar'",
    "dangerous_query4": "--'- : +--+ / : -- - : --+- : /*",
    # "dangerous_query5": ""
}

