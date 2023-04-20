#!/usr/bin/env python3

import pymysql
import cgi
import cgitb
#We need json to create the final json object 
import json

#the next line is useful for debugging
#it causes errors during execution to be sent back to the browser
cgitb.enable()

# We will have 2 queries: one for the target scores histogram and another for the gene sequence search to produce the table
query1 = """
SELECT t.score 
FROM targets t JOIN gene g using(gid)
WHERE g.name = %s
"""

query2 = """
SELECT name, chr, start, stop 
FROM gene g 
WHERE seq REGEXP %s
ORDER BY chr, start ASC
"""

#retrieve input data from the web server
form = cgi.FieldStorage() 

#next line is always required as first part of http output
print("Content-type: text/html\n")

# First we need to connect to the database
connection = pymysql.connect(
            host = "bioed.bu.edu",
            user = 'sv',
            password = 'sv', 
            db = 'miRNA', 
            port = 4253, 
            autocommit=True 
            )


if (form):       
     # get cursor
    cursor = connection.cursor()
    # We create a selector variable that will decide if we are to use the histogram producing query 
    # or the gene sequence search query
    selector = form.getvalue("selector","")

    if (selector == "histogram"):
        gene = form.getvalue("gene","")
        if(gene!=""):
            #execute query
            try: 
                #Execute query1 using gene user input 
                cursor.execute(query1,[gene])
            except pymysql.Error as e: 
                print(e)
        
            results = cursor.fetchall() 
            #format the output as json object
            print(json.dumps(results))

    if (selector == "regexp_table"):
        dna_sequence = form.getvalue("dna_sequence","")
        if(dna_sequence!=""):
            #execute query
            try: 
                #Execute query2 using dna_sequence user input 
                cursor.execute(query2,[dna_sequence])
            except pymysql.Error as e: 
                print(e)
        
            results = cursor.fetchall() 
            #format the output as json object
            print(json.dumps(results))


        
