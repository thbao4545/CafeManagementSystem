class Deparment:
	def __init__(self, ID, name):
		self.ID = ID
		self.name = name

class Staff:
	info = None
	def __init__(self, info):
		self.ID = info["ID"]
		self.name = info["name"]
		self.gender = info["gender"]
		self.birthday = info["birthday"]
		self.address = info["address"]
		self.startingDay = info["startingDay"]
		self.deparment = info["deparment"]

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
		info = dict(ID = self.ID, name = self.name, gender = self.gender, )

if __name__ == '__main__':
	info = dict(ID = 1, name = "Khang", gender = 0, birthday = "28-05-2003", address = "TV", 
		startingDay = "4-2", deparment = Deparment(1, "Moc boc"))

	newStaff = Staff(info)
	print(info.values())
