import csv
import sys
import psycopg2

def insert_into_db(fname):
    f = open(fname, 'r+')
    data = csv.reader(f)

    conn = psycopg2.connect("dbname = superhero user = hmj")
    cur = conn.cursor()
    cur.execute("drop table heros;")
    cur.execute("create table heros (id serial primary key, name text, gender varchar(1));")

    for row in data:
        cur.execute("insert into heros (name, gender) values (%s, %s)",(row[0], row[1]))

    cur.execute("select * from heros;")
    for id, name, gender in cur.fetchall():
        print(name, gender)

    if (len(sys.argv) == 4):
        wdata = csv.writer(f)
        wdata.writerow([sys.argv[2], sys.argv[3]])
    
    conn.commit()
    cur.close()
    conn.close()

    f.close()

def main():
    insert_into_db(sys.argv[1])


if (__name__ == "__main__"):
    main()

