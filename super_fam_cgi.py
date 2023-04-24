#!/usr/bin/env python3

# settings-------------------------------------------

import pymysql
import cgi
import cgitb
import json

#----------------------------------------------------

# enabling debugging
cgitb.enable()


form = cgi.FieldStorage()
selector = 'piechart'

# print("Content-type: text/html\n")
print("Content-type: application/json\n")

sf_query = """
SELECT rt.repeat_superfamily, count(rt.repeat_superfamily) as Total
FROM `Sequence` s JOIN Repeat_Type rt ON s.TID = rt.TID 
WHERE rt.repeat_class = %s
GROUP BY rt.repeat_order 
"""

if (form):
	class_choice = form.getvalue('class_choice', '')
	if (class_choice != ''):
		try:
			# connect to database if `class_choice` is filled
			connection = pymysql.connect(
				host = 'bioed.bu.edu',
				user = 'carvalhd',
				password = 'carvalhd',
				db = 'Team_H',
				port = 4253)
		except pymysql.Error as e:
			print(e)
		cursor = connection.cursor()
		try:
			cursor.execute(sf_query, [class_choice])
		except pymysql.Error as e:
			print(e, sf_query)
			
		results = cursor.fetchall()
		
		# results to json format
		print(json.dumps(results))