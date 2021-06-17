import pyexcel_ods as pods
import psycopg2
import sys

def insert_into_db(fname):
    data = pods.get_data(fname)

    conn = psycopg2.connect("dbname = superhero user = hmj")
    cur = conn.cursor()
    cur.execute("drop table heros;")
    cur.execute("create table heros (id serial primary key, name text, gender varchar(1));")

    #for v in json.loads((json.dumps(data))).values(): -> this can also be used
    #json.loads will take a string(json.dumps returns data as string) and give data in dictionary format. here we get {"Sheet1" : [[row1 values], [row2 values], ...[rown values]], "Sheet 2" : [],"Sheet3" : []......so on }
    for v in data.values():    
        for value in v:
            cur.execute("insert into heros (name, gender) values (%s, %s)",(value[0], value[1]))

    cur.execute("select * from heros;")
    for id, name, gender in cur.fetchall(): #cur.fetchall() can be used to fetch all the rows of a query result
        print(name, gender)

    if(len(sys.argv) == 4):
        
        data["Sheet1"].append([sys.argv[2], sys.argv[3]]) #sys.argv[2] is the name of the hero and sys.argv[3] is the gender
        pods.save_data(fname, data)

    conn.commit()
    cur.close()
    conn.close()

def main():
    insert_into_db(sys.argv[1]) #sys.argv can be used to take command line arguments. NOTE : sys.argv[0] is the python file name by default.
    #sys.argv[1] is the name of the spreadsheet file 

if (__name__ == "__main__"):
    main()
