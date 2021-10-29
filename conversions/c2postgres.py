import pandas as pd
from sqlalchemy import create_engine
import psycopg2

operation = input (" press 1 to import or 2 to export ")
df=pd.read_csv('sample.csv',encoding='iso-8859-1')
def import(df):
    try:       
        df.columns=[c.lower() for c in df.columns]
        print("create tables\n...")
        engine=create_engine('postgresql://postgres:urp4ss@localhost:5432/urdb')
        df.to_sql("sample_camp",con=engine,index=False)
        return True
    except ValueError:
        return 'Our script is died'
def export():
    try:
       conn=psycopg2.connect("host=localhost dbname=sampledb user=postgres password=r00t")
       cur=conn.cursor()
       cur.execute('SELECT * FROM sample_camp')
       _all=cur.fetchall()
       with open('sample-exprt.csv','w',newline='') as fp:
            a=csv.writer(fp,delimiter=',')
       for line in _all:
            a.writerows(line)
       return True
    except ValueError:
        return 'perharps that we dont conect the db'
cur.close()
conn.close()

    
