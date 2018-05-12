


import pandas as pd
df = pd.read_csv('https://download.bls.gov/pub/time.series/cu/cu.item',sep='\t')



df = pd.read_csv('s3://pandas-test/tips.csv')


Writing to CSV format
write_csv

xlsx = pd.ExcelFile('path_to_file.xls')
df = pd.read_excel(xlsx, 'Sheet1')with pd.ExcelFile('path_to_file.xls') as xls:
    df1 = pd.read_excel(xls, 'Sheet1')
    df2 = pd.read_excel(xls, 'Sheet2')data.to_sql('data', engine)
read_sql_table(table_name, con[, schema, …])df.to_sql('table', engine, schema='other_schema')
pd.read_sql_table('table', engine, schema='other_schema')pd.read_sql_query('SELECT * FROM data', engine)
pd.read_sql_query("SELECT id, Col_1, Col_2 FROM data WHERE id = 42;", engine)from sqlalchemy import create_engine

engine = create_engine('postgresql://scott:tiger@localhost:5432/mydatabase')

engine = create_engine('mysql+mysqldb://scott:tiger@localhost/foo')

engine = create_engine('oracle://scott:tiger@127.0.0.1:1521/sidname')

engine = create_engine('mssql+pyodbc://mydsn')

# sqlite://<nohostname>/<path>
# where <path> is relative:
engine = create_engine('sqlite:///foo.db')

# or absolute, starting with a slash:
engine = create_engine('sqlite:////absolute/path/to/foo.db')
# In[ ]:



