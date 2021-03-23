from .__init__ import app
from sqlalchemy import Table, Column, Integer, String, DateTime, Float, create_engine, Boolean, MetaData, Unicode

try:   
    engine = create_engine("mysql://root:@localhost/")
    conn = engine.connect()
    conn.execute("commit")
    conn.execute("create database properties;")
    conn.close()
except Exception as e:
    print("An error occurred, error details:\n---------------------\n{}\n---------------------\n".format(e))

try:
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo = False)
except Exception as e:
    
    print("An error occurred, error details:\n---------------------\n{}\n---------------------\n".format(e))
    exit(1)
meta = MetaData()


def query(sql):
    print("Query: '{}'".format(sql))
    results = "An error occurred.\n"
    with engine.connect() as connection:
        try:
            results = connection.execute(sql)
        except Exception as e:
            
            print("An error occurred, error details:\n---------------------\n{}\n---------------------\n".format(e))
    return results

properties = Table(
    'properties', meta,
    Column('prop_id', Integer, primary_key=True),
    Column('title', String),
    Column('no_bed', Integer),
    Column('no_bath', Integer),
    Column('loc', String),
    Column('typ', String),
    Column('descr', String),
    Column('price', Float),
    Column('media_addr', String)
)

meta.create_all(engine)