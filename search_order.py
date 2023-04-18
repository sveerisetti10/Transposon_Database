#!/usr/bin/env python3

import pymysql
import cgi
import cgitb
import json

cgitb.enable()

query1 = """
SELECT repeat_type as Transposon_Order, count(*) as Total
FROM {}
GROUP BY repeat_type
ORDER BY Total DESC
"""

form = cgi.FieldStorage()

print("Content-Type: application/json")
print()

connection = pymysql.connect(
    host="bioed.bu.edu",
    user='sv',
    password='sv',
    db='Team_H',
    port=4253,
    autocommit=True
)

if form:
    cursor = connection.cursor()
    selector = form.getvalue("selector", "")

    if selector == "histogram":
        sequence = form.getvalue("sequence", "")
        if sequence != "":
            formatted_query = query1.format(sequence)
            try:
                cursor.execute(formatted_query)
            except pymysql.Error as e:
                response = {"error": str(e)}
                print(json.dumps(response))
                exit()

            results = cursor.fetchall()
            results_list = [[row[0], row[1]] for row in results]

            print(json.dumps(results_list))
        else:
            response = {"error": "Empty sequence"}
            print(json.dumps(response))
    else:
        response = {"error": "Invalid selector"}
        print(json.dumps(response))
else:
    response = {"error": "No form data received"}
    print(json.dumps(response))
