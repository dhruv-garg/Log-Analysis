#!/usr/bin/env python

import psycopg2
import time

# Initializing Queries
# We have to view only top3 popular authors
q1 = "SELECT title, total_views FROM view1 limit 3"

# We have to view only top popular article authors of all time
q2 = """SELECT authors.name,sum(view1.total_views) AS total_views from view1,
        authors WHERE authors.id = view1.author GROUP BY authors.name
        ORDER BY total_views desc"""

# Days which did more than 1% of requests leading to errors
q3 = """SELECT to_char(date,'MM DD,YYYY') AS date,view4.Percent_Error
        from view4 WHERE view4.Percent_Error>1.0"""

print("")

# Popular Articles
print("Most Popular Three Articles Of All Time:")
db = psycopg2.connect("dbname = news")
c1 = db.cursor()
c1.execute(q1)
output = c1.fetchall()
for i in range(0, len(output)):
    article_title = output[i][0]
    total_views = output[i][1]
    print("%d) %s -> %d" % (i+1, article_title, total_views)+" views")
db.close()
# ------------------------------------------------------------------------------

print("")
# Popular Authors
print("Most Popular Article Authors Of All Time:")
db = psycopg2.connect("dbname = news")
c2 = db.cursor()
c2.execute(q2)
output = c2.fetchall()
for i in range(0, len(output)):
    author_name = output[i][0]
    total_views = output[i][1]
    print("%d) %s -> %d" % (i+1, author_name, total_views)+" views")
db.close()
# ------------------------------------------------------------------------------

print("")
# Error Days
print("HTTP Status Code:")
db = psycopg2.connect("dbname = news")
c3 = db.cursor()
c3.execute(q3)
output = c3.fetchall()
for i in range(0, len(output)):
    date = output[i][0]
    error = output[i][1]
    print("%s, %.1f%%" % (date, error)+" errors")
db.close()
print("")
