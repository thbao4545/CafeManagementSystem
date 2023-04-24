from copy import deepcopy
from Deparment import Deparment

class Staff:
	def __init__(self, info):
		self.ID = info["ID"] 												#ID
		self.name = info["name"]  											#Ten
		self.gender = info["gender"]  										#Gioi tinh
		self.birthday = info["birthday"]									#Ngay sinh
		self.address = info["address"]										#Que quan
		self.startingDay = info["startingDay"]								#Ngay bat dau lam viec
		self.deparment = deepcopy(info["deparment"])						#

	def __str__(self):
		return f"[{self.ID}]{self.name} - Position: {self.deparment.name}"

	def updateInfo(self, info):
		self.ID = info["ID"]
		self.name = info["name"]
		self.gender = info["gender"]
		self.birthday = info["birthday"]
		self.address = info["address"]
		self.startingDay = info["startingDay"]
		self.deparment = info["deparment"]

	def getInfo(self):
		info = dict(ID = self.ID, name = self.name, gender = self.gender, birthday = self.birthday,
						address = self.address, startingDay = self.startingDay, deparment = deepcopy(self.deparment))
		return info

if __name__ == '__main__':
	# info = dict(ID = 1, name = "Khang", gender = 0, birthday = "28-05-2003", address = "TV", 
	# 	startingDay = "4-2", deparment = Deparment(1, "Moc boc"))

	# newInfo = dict(ID = 2, name = "Puken", gender = 0, birthday = "28-05-2003", address = "TV", 
	# 	startingDay = "4-2", deparment = Deparment(1, "Moc boc"))
	# newStaff = Staff(info)
	# anotherStaff = deepcopy(newStaff)
	# anotherStaff.updateInfo(newInfo)

	# print(newStaff.getInfo())
	# print(anotherStaff.getInfo())