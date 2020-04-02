import sqlite3
import os
import sys
dirname = os.path.dirname(os.path.abspath(__file__))
sys.path.append(dirname)

def create_database():
	try:
		conn = sqlite3.connect(dirname+'link_cache.db')  
		c = conn.cursor()
		c.execute('CREATE TABLE youtube (link varchar(255) PRIMARY KEY, converted text)')
		conn.commit()
		return ("Created database",True)
	except Exception as e:
		return(e,False)

def check_cache(link):
	conn = sqlite3.connect(dirname+'link_cache.db')  
	c = conn.cursor()
	try:
		c.execute("select converted from youtube where link = '%s'"%(link))
		converted = c.fetchall()
		if converted:
			return (converted[0][0],True)
		else:
			return("Not found",False)
	except Exception as e:
		if 'no such table' in str(e):
			error,status = create_database()	
		return (str(e)+':'+str(error),False)

def cache(link,text):
	conn = sqlite3.connect(dirname+'link_cache.db')  
	c = conn.cursor()
	try:
		c.execute("insert into youtube values ('%s','%s')"%(link,text))
		conn.commit()
		return ("Succesfully cached",True)
	except Exception as e:
		if 'no such table' in str(e):
			error,status = create_database()
			if status == True:
				return cache(link,text)
		else:
			return (e,False)

