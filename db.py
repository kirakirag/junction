import psycopg2
import pandas as pd
from sqlalchemy import create_engine

db_name = "junctionX_hackathon".lower()

def getCredentials():
	lines = []
	with open("postgres_credentials.txt", "r", encoding="utf-8") as f: 
		lines = [line.rstrip("\n") for line in f]
	return lines

def getConnection():
	credentials = getCredentials()
	conn = psycopg2.connect(
		host=credentials[0],
		user=credentials[1],
		password=credentials[2],
		port=credentials[3],
		dbname=db_name
	)
	conn.autocommit = True
	return conn

def ensureDbExists():
	credentials = getCredentials()
	conn = psycopg2.connect(
		host=credentials[0],
		user=credentials[1],
		password=credentials[2],
		port=credentials[3]
	)
	conn.autocommit = True

	cur = conn.cursor()
	cur.execute("SELECT 1 FROM pg_database WHERE datname=%s;", (db_name,))
	exists = cur.fetchone() is not None
	if not exists:
		cur.execute(f"CREATE DATABASE {db_name};")
	cur.close()

def loadData():
	engine = create_engine(f"postgresql+psycopg2://postgres:{getCredentials()[2]}@localhost/{db_name}")
	xls = pd.ExcelFile("data/uber_hackathon_v2_mock_data.xlsx")
	for sheet_name in xls.sheet_names:
		df = pd.read_excel(xls, sheet_name=sheet_name)
		df.to_sql(sheet_name, engine, if_exists="replace", index=False)

def getData(conn, dateStr, cityId):
	cur = conn.cursor()
	cur.execute("""
		Select count(*) from rides_trips 
		where date=%s 
		and city_id=%s
	""", (dateStr, cityId,))
	return cur.fetchone()[0]
