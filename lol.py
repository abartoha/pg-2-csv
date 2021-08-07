import sys, psycopg2

conn = psycopg2.connect("dbname=testdb1 user=postgres password=loldafaq")

cur = conn.cursor()

sql = "COPY (SELECT * FROM data) TO STDOUT WITH CSV DELIMITER ','"

with open("table.csv", "w+") as file:
    
    cur.copy_expert(sql, file)

cur.close()
