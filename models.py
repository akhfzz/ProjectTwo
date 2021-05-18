import config
import pymysql

db = cursor = None


class User:
	def openDB(self):
		global db, cursor
		db = pymysql.connect(
				host=config.DB_HOST,
				user=config.DB_USER,
				password=config.DB_PASSWORD,
				database=config.DB_NAME
			)
		cursor = db.cursor()

	def closeDB(self):
		global db 
		db.close()

	def LoginPDB(self, name):
		self.openDB()
		container = []
		cursor.execute("SELECT idUser, namaUser, password, email FROM user where namaUser='{0}'".format(name))
		for id, nama, password, email in cursor.fetchall():
			container.append((id, nama, password, email))
		self.closeDB()
		return container

	# def searchDB(self, data):
	# 	self.openDB()
	# 	container = []
	# 	date = cursor.execute("SELECT namaUser FROM user where namaUser='{0}'".format(data))
	# 	for i in date:
	# 		container.append(date)
	# 	self.closeDB()
	# 	return container

	def insertDB(self, data):
		self.openDB()
		cursor.execute("INSERT INTO user (namaUser, password, email) values ('{0}', '{1}', '{2}')".format(data[0], data[1], data[2]))
		db.commit()
		self.closeDB()

class EBook(User):
	def __init__(self, judul=None, tahun=None, type=None, file=None, idUser=None):
		self.judul = judul
		self.tahun = tahun
		self.type = type
		self.file = file
		self.idUser = idUser

	def InsertDB(self, data):
		self.openDB()
		cursor.execute("INSERT INTO eBook (judul, tahun, type, file, idUser) values ('{0}', '{1}', '{2}', '{3}', '{4}')".format(data[0], data[1], data[2], data[3], data[4]))
		db.commit()
		self.closeDB()

	def selectEBook(self, id):
		self.openDB()
		cursor.execute("SELECT idUser, judul, type, tahun, file from ebook where idUser='{0}'".format(id))
		data = cursor.fetchall()
		container = []
		for idUser, judul, type, tahun, file in data:
			container.append((idUser, judul, type, tahun, file))
		return container

	def deleteDB(self, id):
		self.openDB()
		cursor.execute("DELETE FROM ebook where judul='{0}'".format(id))
		db.commit()
		self.closeDB()

	def selectAll(self):
		self.openDB()
		cursor.execute("SELECT idFile, judul, type, tahun, file from ebook")
		data = cursor.fetchall()
		container = []
		for idFile, judul, type, tahun, file in data:
			container.append((idFile, judul, type, tahun, file))
		return container

	def getDBId(self, id):
		self.openDB()
		cursor.execute("SELECT * FROM ebook where idUser='{0}'".format(id))
		data = cursor.fetchone()
		self.closeDB()
		return data

	def updateDB(self, data):
		self.openDB()
		cursor.execute("UPDATE ebook set judul='{0}', type='{1}', tahun='{2}', file='{3}' where idUser='{4}'".format(data[0], data[1], data[2], data[3], data[4]))
		db.commit()
		self.closeDB()

	def searchDB(self, name):
		self.openDB()
		cursor.execute("SELECT * FROM ebook where judul like '%{0}%' ORDER BY judul ASC".format(name))
		data = cursor.fetchone()
		self.closeDB()
		return data

	def selectRelation(self):
		self.openDB()
		container = []
		cursor.execute("SELECT u.email, u.namaUser,e.judul, e.type, e.tahun, e.file from ebook e, user u where e.idUser=u.idUser")
		data = cursor.fetchall()
		for email, namaUser, judul, type, tahun, file in data:
			container.append((email, namaUser, judul, type, tahun, file))
		self.closeDB()
		return container 

class Komunitas(User):
	def insertKom(self, data):
		self.openDB()
		cursor.execute("INSERT INTO community (namaKomunitas, urlKomunitas) values ('{0}', '{1}')".format(data[0], data[1]))
		db.commit()
		self.closeDB()

	def joinKom(self, data):
		self.openDB()
		cursor.execute("INSERT INTO relatecommunity (namaKomunitas, idUser) values ('{0}', '{1}')".format(data[0], data[1]))
		db.commit()
		self.closeDB()

	def selectAll(self):
		self.openDB()
		cursor.execute("SELECT k.namaKomunitas, k.urlKomunitas, COUNT(r.idUser) from community k, relatecommunity r where k.namaKomunitas=r.namaKomunitas GROUP BY r.namaKomunitas")
		data = cursor.fetchall()
		container = []
		for namaKomunitas, urlKomunitas, jumlah in data:
			container.append((namaKomunitas, urlKomunitas, jumlah))
		return container
	def deleteDB(self, id):
		self.openDB()
		cursor.execute("DELETE FROM community where namaKomunitas='{0}'".format(id))
		db.commit()
		self.closeDB()

	def selectAllDB(self):
		self.openDB()
		cursor.execute("SELECT namaKomunitas, urlKomunitas from community")
		data = cursor.fetchall()
		container = []
		for nama, url in data:
			container.append((nama, url))
		return container

