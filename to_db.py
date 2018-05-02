# -*- coding: utf-8 -*-

# to_db.py
__author__ = 'adrian aley'

import MySQLdb as mdb # MySQL server and database storage
from pandas.io import sql

# obtain a database connection to the mysql instance
db_host = 'localhost'
db_user = 'username'
db_pass = 'password'
db_name = 'stock_master'
con = mdb.connect(db_host, db_user, db_pass, db_name)

df.to_sql(con=con, name='stock_data', if_exists='replace', flavor='mysql')
