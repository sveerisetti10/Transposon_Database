#!/usr/bin/env python3

import json
import pymysql
import cgi

# Connect to database
connection = pymysql.connect(
    host="bioed.bu.edu",
    user="sv",
    password="sv",
    db="Team_H",
    port=4253,
    autocommit=True,
)

# Define SQL query
# Here we allow the user to enter in a value for what table information they would like to display
query1 = """
SELECT repeat_type as Transposon_Order, count(*) as Total
FROM `{}` 
GROUP BY repeat_type
ORDER BY Total DESC
"""

# Process form data
form = cgi.FieldStorage()
#Checking to see that both the selector and the table of choice are indeed valid inputs
if "selector" in form and "table_choice" in form:
    selector = form.getvalue("selector", "")
    table_choice = form.getvalue("table_choice")

    # If the selector is "piechart", then we need to execute the query about and return a JSON file 
    if selector == "piechart":
        try:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute(query1.format(table_choice))
                results = cursor.fetchall()
                print("Content-type: application/json\n")
                #Create our JSON file that contains the data needed to produce the pie chart
                print(json.dumps(results))
        except (pymysql.Error, TypeError) as e:
            print("Content-type: text/plain\n")
            print(f"An error occurred: {e}")
