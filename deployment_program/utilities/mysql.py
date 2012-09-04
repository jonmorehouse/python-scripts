import MySQLdb as mysql

# import _mysql #_mysql is the c api -- does not use the python db api
import sys

class Mysql(object):
	
	# CONFIG DATA
	host = "localhost"
	username = "DefaultPassword"
	password = "DefaultPassword"
	port = False
	con = None
	
	# PRIVATE FUNCTIONS
		
	def __init__(self, database):
		
		self.database = database
		self.__connect()
		self.__clear()
		
		
		
	
	
	def __del__(self):
		
		if self.con:
			self.con.close()
			
	
	
	def __connect(self):
		
		try:
			self.con = mysql.connect(self.host, self.username, self.password, self.database)
			
		
		except mysql.Error, e:
			
			print "Error %d: %s" % (e.args[0], e.args[1])
			self.__del__()
		
		return self
	
	
	def __clear(self):
		
		self.where_statement = ""
		self.select_statement = "SELECT*"
		
		return self
		
		
	# PUBLIC FUNCTIONS
	
	
	# QUERY BUILDERS
	
	def where(self, column, value, _type = "and"):#WHERE STATEMENT GENERATION 
		
		
		if len(self.where_statement) is 0:
			statement = "where "
			
		elif _type == "and":
			statement = " and "
			
		else:
			statement = " or "
		
		if isinstance(value, str):
			statement += "%s = '%s'" % (column, value)
		
		else: # a boolean = need to take care of the 'double' values
			statement += "%s = %s" % (column, value)
			
			
		self.where_statement += statement 
						
		return self
	
	
	def select(self, columns):#SELECT STATEMENT
		
		self.select_statement = "" # take out the * because this was called!
		
		statement = self.select_statement
		
		if len(statement) is 0:
			statement = "SELECT "
			
		if isinstance(columns, str):
			statement += " %s" %columns
			
		else:
			for column in columns:
				statement += "%s" % column
				
				if column != columns[-1]:
					statement += ", "
		
		self.select_statement += statement
		
		
		return self
	
	
	def join(self):pass #JOIN FUNCTIONALITY COMING AT A LATER TIME
	
	
	# EXECUTION FUNCTOINS
		
	def get(self, table):#
		# ASSUMING THAT WE HAVE APPLIED A WHERE STATEMENT
		
		statement = "%s FROM %s %s;" % (self.select_statement, table, self.where_statement)
						
		query = self.con.cursor(mysql.cursors.DictCursor)
		
		query.execute(statement)
					
		self.__clear() #clear the qeued up where/select statement
		
		rows = int(query.rowcount)
		
		if rows == 0:
			return False
		else:
			return query.fetchall()
		
	
	
	def update(self, table, column, value):
		
		statement = "update %s set %s = %s %s;" % (table, column, value, self.where_statement)
		update = self.con.execute(statement)
		
		self._clear()
		
		return update		
		
	
	
	def insert(self, table, values, columns = False):#will assume that we are working with all values if no columns passed
		
		statement = "Insert into %s" % table
		
		# generate columns if they are specified, otherwise just assume that not being used in this application
		if columns:
			statement += " ("
			
			for column in columns:
				statement += column
				
				if column != columns[-1]:
					statement += ", "
			statement += ")"
		
		# generate the actual values segment
		statement += " values ("
		
		for value in values:
			
			if isinstance(value, str):
				statement += "'%s'" % value
			else:
				statement += "%s" % str(value)
			
			if value != values[-1]:
				statement += ", "
				
		statement += ");"
		
		insert = self.con.cursor()
		insert.execute(statement)
		
		self.con.commit() #actually submit the changes
		
		return insert.rowcount
		
		
	
	
	def unique(self, table, category):
		
		statement = "Select distinct (%s) from %s;" %(category, table)
		
		query = self.con.cursor(mysql.cursors.DictCursor)
		query.execute(statement)
		
		self.__clear()
		
		return query.fetchall()
	
	
	def delete(self, table):
		
		statement = "Delete from %s %s;" % (table, self.where_statement)
		
		delete = self.con.cursor()
		
		delete.execute(statement)
			
		self.con.commit()
						
		self.__clear()
		
		return delete.rowcount
	
		
		
		
		
# END OBJECT






	



	
	


	
	
