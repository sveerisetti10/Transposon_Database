#!/usr/bin/env python3

import cgi
import json
from string import Template
import pymysql
import cgitb
#----------------------------------------------------

# enabling debugging
cgitb.enable()


form = cgi.FieldStorage()
selector = 'piechart'

# print("Content-type: text/html\n")
print("Content-type: application/json\n")

species_class = Template("""SELECT rt.repeat_class,count(*) as count
                            FROM `Sequence` s join Repeat_Type rt on s.TID = rt.TID JOIN Species s2 ON s.SPID = s2.SPID  
                            WHERE s2.species_name = '${sname}'
                            GROUP BY  rt.repeat_class""")

species_order = Template("""SELECT rt.repeat_order, count(*) as count
                            FROM `Sequence` s join Repeat_Type rt on s.TID = rt.TID JOIN Species s2 ON s.SPID = s2.SPID  
                            WHERE s2.species_name = '${sname}'
                            GROUP BY  rt.repeat_order""")

species_superfamily = Template("""SELECT rt.repeat_superfamily, count(*) as count
                                FROM `Sequence` s join Repeat_Type rt on s.TID = rt.TID JOIN Species s2 ON s.SPID = s2.SPID  
                                WHERE s2.species_name = '${sname}'
                                GROUP BY  rt.repeat_superfamily""")

species_length = Template("""SELECT s.`length`
                            FROM `Sequence` s join Repeat_Type rt on s.TID = rt.TID JOIN Species s2 ON s.SPID = s2.SPID  
                            WHERE s2.species_name = '${sname}'
                            ORDER BY s.`length` ASC""")

output = {}


species = form.getvalue("species")

if species == "Homo+sapiens":
    species = "Homo sapiens"

if species == "Heterocephalus+glaber":
    species = "Heterocephalus glaber"

if species == "Betta+splendens":
    species = "Betta splendens"

if species == "Takifugu+rubripes":
    species = "Takifugu rubripes"


	
# connect to database if `class_choice` is filled
connection = pymysql.connect(
    host = 'bioed.bu.edu',
    user = 'saravind',
    password = 'saravind',
    db = 'Team_H',
    port = 4253)
			

cursor = connection.cursor()

cursor.execute(species_class.safe_substitute(sname = species))	
output['class'] = cursor.fetchall()
# results = cursor.fetchall()

cursor.execute(species_order.safe_substitute(sname = species))
output['order'] = cursor.fetchall()

cursor.execute(species_superfamily.safe_substitute(sname = species))
output['superfamily'] = cursor.fetchall()

cursor.execute(species_length.safe_substitute(sname = species))
output['length'] = cursor.fetchall()

# results to json format
print(json.dumps(output))