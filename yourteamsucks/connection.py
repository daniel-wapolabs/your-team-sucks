import sqlalchemy


dbms = 'mysql'
host = 'yourteamsucks-dev.crl3ponxvghl.us-east-1.rds.amazonaws.com'
user = 'wapolabsdb'
password = 'wapocloud1'
database = 'yourteamsucks'

dbms = 'mysql'
host = 'localhost'
user = 'root'
password = ''
database = 'test'

engine_path = '{dbms}://{user}:{pwd}@{host}/{dbname}'.format(
	dbms=dbms,
	host=host,
	user=user,
	pwd=password,
	dbname=database
)
engine = sqlalchemy.create_engine(engine_path)
