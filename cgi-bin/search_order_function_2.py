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

# Define the SQL queries
# Here we allow the user to enter in a value for what table information they would like to display
query1 = """
SELECT s2.species_name as Species, repeat_type as Transposon_Order, count(*) as Count
FROM `Sequence` s JOIN Repeat_Type rt using(TID)
JOIN Species s2 using (SPID)
WHERE repeat_type REGEXP '{}'
GROUP BY s.SPID
ORDER BY Count DESC
"""

# Process form data
form = cgi.FieldStorage()
#Checking to see that both the selector and the table of choice are indeed valid inputs
if "selector" in form and "transposon_choice" in form:
    selector = form.getvalue("selector", "")
    transposon_choice = form.getvalue("transposon_choice")

    # If the selector is "piechart", then we need to execute the query about and return a JSON file 
    if selector == "piechart_specific":
        try:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute(query1.format(transposon_choice))
                results = cursor.fetchall()
                print("Content-type: application/json\n")
                #Create our JSON file that contains the data needed to produce the pie chart
                print(json.dumps(results))
        except (pymysql.Error, TypeError) as e:
            print("Content-type: text/plain\n")
            print(f"An error occurred: {e}")

