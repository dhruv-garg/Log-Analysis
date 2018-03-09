About
In this project, a large database with millions of rows is explored by building
complex SQL Queries to fetch data.We build build an internal reporting tool
that will use information from the database to discover what kind of articles
the site's readers like.

Prerequisites:
1) PostgreSQL
Read Here: https://www.postgresql.org/docs/9.5/static/
2) Virtual Box
Download from here: https://www.virtualbox.org/wiki/Downloads
3) Vagrant
Download from here: https://www.vagrantup.com/downloads.html

Launching the machine:
1) $ vagrant up
2) Then login using this command:
   $vagrant ssh
3) Change directory with /vagrant and look for files with list(ls) command.

Load data in database:
psql -d news -f newsdata.sql

There are three tables in database:
1) Articles Table
Columns: author, title, slug, lead, body, time, id
2) Authors Table
Columns: name, bio, id
3) Log Table
Columns: path, ip, method, status, time, id

Use psql -d news to connect to database

Creating Views:
1) Creating first view:
Command:  create view view1 as select title, author, count(title) as total_views
          from articles, log where log.path like concat('%',articles.slug)
          group by articles.title, articles.author order by total_views desc;

2) Creating second view:
Command: create view view4 as select date(time),
          round(100.0*sum(case log.status when '200 OK' then 0 else 1 end)/count(log.status),2)
          as Percent_Error from log group by date(time)
          order by Percent_Error desc;

Come out of database : Ctrl+d

Running Python File:
python log_analysis.py
# Log-Analysis
